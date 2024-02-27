from django.urls import path
from .views import (
    MissionListCreateView, MissionDetailView,
    CropListCreateView, CropDetailView,
    PlotListCreateView, PlotDetailView,
    PlotIndicesListCreateView, PlotIndicesDetailView,
    ImageOutListCreateView, ImageOutDetailView,
    EdgeStateMachineStatusListCreateView, EdgeStateMachineStatusDetailView,
    CloudStateMachineStatusListCreateView, CloudStateMachineStatusDetailView,
    DroneStatusListCreateView, DroneStatusDetailView,
)

urlpatterns = [
    path('missions/', MissionListCreateView.as_view(), name='mission-list'),
    path('missions/<int:pk>/', MissionDetailView.as_view(), name='mission-detail'),
    path('crops/', CropListCreateView.as_view(), name='crop-list'),
    path('crops/<int:pk>/', CropDetailView.as_view(), name='crop-detail'),
    path('plots/', PlotListCreateView.as_view(), name='plot-list'),
    path('plots/<int:pk>/', PlotDetailView.as_view(), name='plot-detail'),
    path('plotindices/', PlotIndicesListCreateView.as_view(), name='plotindices-list'),
    path('plotindices/<int:pk>/', PlotIndicesDetailView.as_view(), name='plotindices-detail'),
    path('imageout/', ImageOutListCreateView.as_view(), name='imageout-list'),
    path('imageout/<int:pk>/', ImageOutDetailView.as_view(), name='imageout-detail'),
    path('edgestatemachinestatus/', EdgeStateMachineStatusListCreateView.as_view(), name='edgestatemachinestatus-list'),
    path('edgestatemachinestatus/<int:pk>/', EdgeStateMachineStatusDetailView.as_view(), name='edgestatemachinestatus-detail'),
    path('cloudstatemachinestatus/', CloudStateMachineStatusListCreateView.as_view(), name='cloudstatemachinestatus-list'),
    path('cloudstatemachinestatus/<int:pk>/', CloudStateMachineStatusDetailView.as_view(), name='cloudstatemachinestatus-detail'),
    path('dronestatus/', DroneStatusListCreateView.as_view(), name='dronestatus-list'),
    path('dronestatus/<int:pk>/', DroneStatusDetailView.as_view(), name='dronestatus-detail'),
]

