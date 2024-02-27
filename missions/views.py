from rest_framework import generics
from .models import (Mission, Crop, Plot, PlotIndices, ImageOut, 
                     EdgeStateMachineStatus, CloudStateMachineStatus, DroneStatus)
from .serializers import (MissionSerializer, CropSerializer, PlotSerializer, 
                          PlotIndicesSerializer, ImageOutSerializer,
                          EdgeStateMachineStatusSerializer, CloudStateMachineStatusSerializer, 
                          DroneStatusSerializer)

class MissionListCreateView(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class CropListCreateView(generics.ListCreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class CropDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class PlotListCreateView(generics.ListCreateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

class PlotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

class PlotIndicesListCreateView(generics.ListCreateAPIView):
    queryset = PlotIndices.objects.all()
    serializer_class = PlotIndicesSerializer

class PlotIndicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlotIndices.objects.all()
    serializer_class = PlotIndicesSerializer

class ImageOutListCreateView(generics.ListCreateAPIView):
    queryset = ImageOut.objects.all()
    serializer_class = ImageOutSerializer

class ImageOutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageOut.objects.all()
    serializer_class = ImageOutSerializer

class EdgeStateMachineStatusListCreateView(generics.ListCreateAPIView):
    queryset = EdgeStateMachineStatus.objects.all()
    serializer_class = EdgeStateMachineStatusSerializer

class EdgeStateMachineStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EdgeStateMachineStatus.objects.all()
    serializer_class = EdgeStateMachineStatusSerializer

class CloudStateMachineStatusListCreateView(generics.ListCreateAPIView):
    queryset = CloudStateMachineStatus.objects.all()
    serializer_class = CloudStateMachineStatusSerializer

class CloudStateMachineStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CloudStateMachineStatus.objects.all()
    serializer_class = CloudStateMachineStatusSerializer

class DroneStatusListCreateView(generics.ListCreateAPIView):
    queryset = DroneStatus.objects.all()
    serializer_class = DroneStatusSerializer

class DroneStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneStatus.objects.all()
    serializer_class = DroneStatusSerializer

