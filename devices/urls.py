from django.urls import path
from .views import (
    EdgeComputerListCreateView, EdgeComputerDetailView,
    DroneListCreateView, DroneDetailView,
    HangerListCreateView, HangerDetailView,
    EdgeLogListCreateView, EdgeLogDetailView,
    DroneLogListCreateView, DroneLogDetailView,
    HangerLogListCreateView, HangerLogDetailView,
    SensorListCreateView, SensorDetailView,
    SensorReadingListCreateView, SensorReadingDetailView,
    ChargerListCreateView, ChargerDetailView,
    ChargerLogListCreateView, ChargerLogDetailView,
    ChargerSensorListCreateView, ChargerSensorDetailView,
    ChargerSensorReadingListCreateView, ChargerSensorReadingDetailView,
)
urlpatterns = [
    # URLs for EdgeComputer
    path('edge-computers/', EdgeComputerListCreateView.as_view(), name='edge-computer-list-create'),
    path('edge-computers/<int:pk>/', EdgeComputerDetailView.as_view(), name='edge-computer-detail'),

    # URLs for Drone
    path('drones/', DroneListCreateView.as_view(), name='drone-list-create'),
    path('drones/<int:pk>/', DroneDetailView.as_view(), name='drone-detail'),

    # URLs for Hanger
    path('hangers/', HangerListCreateView.as_view(), name='hanger-list-create'),
    path('hangers/<int:pk>/', HangerDetailView.as_view(), name='hanger-detail'),

    # URLs for EdgeLog
    path('edge-logs/', EdgeLogListCreateView.as_view(), name='edge-log-list-create'),
    path('edge-logs/<int:pk>/', EdgeLogDetailView.as_view(), name='edge-log-detail'),

    # URLs for DroneLog
    path('drone-logs/', DroneLogListCreateView.as_view(), name='drone-log-list-create'),
    path('drone-logs/<int:pk>/', DroneLogDetailView.as_view(), name='drone-log-detail'),

    # URLs for HangerLog
    path('hanger-logs/', HangerLogListCreateView.as_view(), name='hanger-log-list-create'),
    path('hanger-logs/<int:pk>/', HangerLogDetailView.as_view(), name='hanger-log-detail'),

    # URLs for Sensor
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),

    # URLs for SensorReading
    path('sensor-readings/', SensorReadingListCreateView.as_view(), name='sensor-reading-list-create'),
    path('sensor-readings/<int:pk>/', SensorReadingDetailView.as_view(), name='sensor-reading-detail'),

    # URLs for Charger
    path('chargers/', ChargerListCreateView.as_view(), name='charger-list-create'),
    path('chargers/<int:pk>/', ChargerDetailView.as_view(), name='charger-detail'),

    # URLs for ChargerLog
    path('charger-logs/', ChargerLogListCreateView.as_view(), name='charger-log-list-create'),
    path('charger-logs/<int:pk>/', ChargerLogDetailView.as_view(), name='charger-log-detail'),

    # URLs for ChargerSensor
    path('charger-sensors/', ChargerSensorListCreateView.as_view(), name='charger-sensor-list-create'),
    path('charger-sensors/<int:pk>/', ChargerSensorDetailView.as_view(), name='charger-sensor-detail'),

    # URLs for ChargerSensorReading
    path('charger-sensor-readings/', ChargerSensorReadingListCreateView.as_view(), name='charger-sensor-reading-list-create'),
    path('charger-sensor-readings/<int:pk>/', ChargerSensorReadingDetailView.as_view(), name='charger-sensor-reading-detail'),
]


