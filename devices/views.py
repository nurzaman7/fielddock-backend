from rest_framework import generics
from .models import (
    EdgeComputer, Drone, Hanger, EdgeLog, DroneLog, HangerLog,
    Sensor, SensorReading, Charger, ChargerLog, ChargerSensor, ChargerSensorReading
)
from .serializers import (
    EdgeComputerSerializer, DroneSerializer, HangerSerializer,
    EdgeLogSerializer, DroneLogSerializer, HangerLogSerializer,
    SensorSerializer, SensorReadingSerializer,
    ChargerSerializer, ChargerLogSerializer, ChargerSensorSerializer, ChargerSensorReadingSerializer
)



class EdgeComputerListCreateView(generics.ListCreateAPIView):
    queryset = EdgeComputer.objects.all()
    serializer_class = EdgeComputerSerializer

class EdgeComputerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EdgeComputer.objects.all()
    serializer_class = EdgeComputerSerializer

class DroneListCreateView(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class DroneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class HangerListCreateView(generics.ListCreateAPIView):
    queryset = Hanger.objects.all()
    serializer_class = HangerSerializer

class HangerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hanger.objects.all()
    serializer_class = HangerSerializer

class EdgeLogListCreateView(generics.ListCreateAPIView):
    queryset = EdgeLog.objects.all()
    serializer_class = EdgeLogSerializer

class EdgeLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EdgeLog.objects.all()
    serializer_class = EdgeLogSerializer

class DroneLogListCreateView(generics.ListCreateAPIView):
    queryset = DroneLog.objects.all()
    serializer_class = DroneLogSerializer

class DroneLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneLog.objects.all()
    serializer_class = DroneLogSerializer

class HangerLogListCreateView(generics.ListCreateAPIView):
    queryset = HangerLog.objects.all()
    serializer_class = HangerLogSerializer

class HangerLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HangerLog.objects.all()
    serializer_class = HangerLogSerializer

class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorReadingListCreateView(generics.ListCreateAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer

class SensorReadingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
    
    
   
class ChargerListCreateView(generics.ListCreateAPIView):
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer

class ChargerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer

class ChargerLogListCreateView(generics.ListCreateAPIView):
    queryset = ChargerLog.objects.all()
    serializer_class = ChargerLogSerializer

class ChargerLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargerLog.objects.all()
    serializer_class = ChargerLogSerializer

class ChargerSensorListCreateView(generics.ListCreateAPIView):
    queryset = ChargerSensor.objects.all()
    serializer_class = ChargerSensorSerializer

class ChargerSensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargerSensor.objects.all()
    serializer_class = ChargerSensorSerializer

class ChargerSensorReadingListCreateView(generics.ListCreateAPIView):
    queryset = ChargerSensorReading.objects.all()
    serializer_class = ChargerSensorReadingSerializer

class ChargerSensorReadingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargerSensorReading.objects.all()
    serializer_class = ChargerSensorReadingSerializer


