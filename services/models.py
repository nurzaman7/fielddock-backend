# services/models.py

from django.db import models

class GPSLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()  # Altitude in meters
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Altitude: {self.altitude}, Timestamp: {self.timestamp}"

