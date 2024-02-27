from rest_framework import serializers
from .models import (
    EdgeComputer, Drone, Hanger, EdgeLog, DroneLog, HangerLog,
    Sensor, SensorReading, Charger, ChargerLog, ChargerSensor, ChargerSensorReading
)

class EdgeComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdgeComputer
        fields = '__all__'

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

class HangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hanger
        fields = '__all__'

class EdgeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdgeLog
        fields = '__all__'

class DroneLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneLog
        fields = '__all__'

class HangerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HangerLog
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'

class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields = '__all__'

class ChargerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargerLog
        fields = '__all__'

class ChargerSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargerSensor
        fields = '__all__'

class ChargerSensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargerSensorReading
        fields = '__all__'

