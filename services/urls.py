# services/urls.py

from django.urls import path

from .views import FlightSafetyCheckView
from .views import GPSLocationListCreateView, GPSLocationDetailView
from .views import FlightTimeCalculatorView

urlpatterns = [
    path('flight-safety-check/', FlightSafetyCheckView.as_view(), name='flight-safety-check'),
    path('gps-locations/', GPSLocationListCreateView.as_view(), name='gpslocation-list-create'),
    path('gps-locations/<int:pk>/', GPSLocationDetailView.as_view(), name='gpslocation-detail'),
    path('calculate-flight-time/', FlightTimeCalculatorView.as_view(), name='calculate-flight-time'),
]



