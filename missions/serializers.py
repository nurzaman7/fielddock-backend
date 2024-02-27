from rest_framework import serializers
from .models import Mission, Crop, Plot, PlotIndices, ImageOut, EdgeStateMachineStatus, CloudStateMachineStatus, DroneStatus

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'

class PlotIndicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotIndices
        fields = '__all__'

class ImageOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOut
        fields = '__all__'

class EdgeStateMachineStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdgeStateMachineStatus
        fields = '__all__'

class CloudStateMachineStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudStateMachineStatus
        fields = '__all__'

class DroneStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneStatus
        fields = '__all__'

