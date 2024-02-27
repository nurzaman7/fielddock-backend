from django.db import models
from admin_site.models import FieldComponent
import datetime

class EdgeComputer(models.Model):
    field_component = models.ForeignKey(FieldComponent, on_delete=models.CASCADE, related_name='edge_computers')
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    storage_capacity = models.FloatField(blank=True, null=True)
    operating_system = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.serial_number}'

class Drone(models.Model):
    field_component = models.ForeignKey(FieldComponent, on_delete=models.CASCADE, related_name='drones')
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    battery = models.CharField(max_length=50, blank=True, null=True)
    gps_location = models.CharField(max_length=50, blank=True, null=True)
    telemetry_data = models.TextField(blank=True, null=True)
    camera = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.serial_number}'

class Hanger(models.Model):
    field_component = models.ForeignKey(FieldComponent, on_delete=models.CASCADE, related_name='hangers')
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    door_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.serial_number}'

class EdgeLog(models.Model):
    edge_computer = models.ForeignKey(EdgeComputer, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'Log for EdgeComputer {self.edge_computer.name} at {self.timestamp}'

class DroneLog(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'Log for Drone {self.drone.name} at {self.timestamp}'

class HangerLog(models.Model):
    hanger = models.ForeignKey(Hanger, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'Log for Hanger {self.hanger.name} at {self.timestamp}'

class Sensor(models.Model):
    edge_computer = models.ForeignKey(EdgeComputer, on_delete=models.CASCADE, related_name='sensors')
    sensor_type = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    specifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.sensor_type} - Model: {self.model_number}'

class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='readings')
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    value = models.FloatField()
    unit = models.CharField(max_length=50, blank=True, null=True)
    
    
    
class Charger(models.Model):
    field_component = models.ForeignKey(FieldComponent, on_delete=models.CASCADE, related_name='chargers')
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    # Additional fields for Charger can be added here

    def __str__(self):
        return f'{self.name} - {self.serial_number}'
        
        
class ChargerLog(models.Model):
    charger = models.ForeignKey(Charger, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'Log for Charger {self.charger.name} at {self.timestamp}'


class ChargerSensor(models.Model):
    charger = models.ForeignKey(Charger, on_delete=models.CASCADE, related_name='sensors')
    sensor_type = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    specifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.sensor_type} - Model: {self.model_number}'


class ChargerSensorReading(models.Model):
    sensor = models.ForeignKey(ChargerSensor, on_delete=models.CASCADE, related_name='readings')
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    value = models.FloatField()
    unit = models.CharField(max_length=50, blank=True, null=True)


