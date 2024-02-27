# services/serializers.py



from rest_framework import serializers
from .models import GPSLocation

from .models import GPSLocation  # Import your GPSLocation model


class FlightTimeSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", help_text="Flight start time in CST")
    flight_duration = serializers.IntegerField(help_text="Flight duration in minutes")



class GPSLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSLocation
        fields = ['latitude', 'longitude', 'altitude', 'timestamp']


class WaypointSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    altitude = serializers.FloatField(required=False, default=0)

class FlightPathSerializer(serializers.Serializer):
    waypoints = WaypointSerializer(many=True)

