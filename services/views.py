import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import GPSLocation
from .serializers import GPSLocationSerializer, FlightTimeSerializer
from .weather_logic import check_conditions

from .serializers import FlightPathSerializer
from geopy.distance import geodesic


# Set up logging
logger = logging.getLogger('services')

            
class FlightSafetyCheckView(APIView):
    def post(self, request, *args, **kwargs):
        logger.info("Handling POST request for FlightSafetyCheckView")
        serializer = FlightTimeSerializer(data=request.data)
        if serializer.is_valid():
            start_time = serializer.validated_data['start_time']
            flight_duration = serializer.validated_data['flight_duration']
            
            # Assuming check_conditions function now also takes start_time
            real_time_check, forecast_check = check_conditions(start_time, flight_duration)

            logger.info(f"Flight time check results: Real Time: {real_time_check}, Forecast: {forecast_check}")
            return Response({
                "real_time_check": real_time_check,
                "forecast_check": forecast_check
            })
        else:
            logger.warning("Invalid data submitted to FlightSafetyCheckView")
            return Response(serializer.errors, status=400)
            
            

class GPSLocationListCreateView(generics.ListCreateAPIView):
    queryset = GPSLocation.objects.all()
    serializer_class = GPSLocationSerializer

    def get(self, request, *args, **kwargs):
        logger.info("Fetching all GPS locations")
        return super(GPSLocationListCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logger.info("Creating a new GPS location")
        return super(GPSLocationListCreateView, self).post(request, *args, **kwargs)

class GPSLocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPSLocation.objects.all()
    serializer_class = GPSLocationSerializer

    def get(self, request, *args, **kwargs):
        logger.info(f"Fetching GPS location with ID: {kwargs.get('pk')}")
        return super(GPSLocationDetailView, self).get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        logger.info(f"Updating GPS location with ID: {kwargs.get('pk')}")
        return super(GPSLocationDetailView, self).put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        logger.info(f"Deleting GPS location with ID: {kwargs.get('pk')}")
        return super(GPSLocationDetailView, self).delete(request, *args, **kwargs)



class FlightTimeCalculatorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FlightPathSerializer(data=request.data)
        if serializer.is_valid():
            waypoints = serializer.validated_data['waypoints']
            DRONE_SPEED_MPS = 5  # Drone speed in meters per second
            total_distance = 0

            for i in range(len(waypoints) - 1):
                start = (waypoints[i]['latitude'], waypoints[i]['longitude'])
                end = (waypoints[i+1]['latitude'], waypoints[i+1]['longitude'])
                total_distance += geodesic(start, end).meters

            flight_time_minutes = (total_distance / DRONE_SPEED_MPS) / 60
            return Response({"flight_time_minutes": flight_time_minutes})

        return Response(serializer.errors, status=400)

