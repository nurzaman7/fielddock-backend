from django.db import models
from admin_site.models import FieldComponent
from datetime import timedelta
from datetime import datetime 

class Mission(models.Model):
    MISSION_STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    field_component = models.ForeignKey(FieldComponent, on_delete=models.CASCADE, related_name='missions')
    mission_date = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)  # Duration can be null
    mission_status = models.CharField(max_length=20, choices=MISSION_STATUS_CHOICES)
    waypoints = models.TextField()
    waypoints_raw= models.TextField()
    weather_conditions = models.CharField(max_length=255, blank=True, null=True)  # Weather conditions can be null

    def __str__(self):
        return f'Mission {self.pk} - {self.mission_status}'

class Crop(models.Model):
    #mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='crops')
    field_component = models.ForeignKey(FieldComponent, on_delete=models.CASCADE, related_name='crops')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
        
class ImageOut(models.Model):
    # Image types
    IMAGE_TYPES = [
        ('Downsample', 'Downsample'),
        ('Heatmap', 'Heatmap'),
        ('Orthomosaic', 'Orthomosaic'),
    ]

    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='imageout')
    time = models.DateTimeField(default=datetime.now)
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPES)
    #image = models.ImageField(upload_to='imageout_images/')
    image= models.FileField(upload_to='imageout_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.image_type} for Mission {self.mission.pk}'
     
        
class Plot(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='plots')
    plot_number = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f'{self.crop.name} - Plot {self.plot_number}'

        

class PlotIndices(models.Model):
    #plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='plot_indices')
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='plot_indices')
    var = models.CharField(max_length=100)
    row = models.IntegerField()
    col = models.IntegerField()
    area_all = models.FloatField()
    area_veg = models.FloatField()
    geometry = models.TextField()
    mean_blue = models.FloatField()
    mean_green = models.FloatField()
    mean_red = models.FloatField()
    mean_rededge = models.FloatField()
    mean_nir = models.FloatField()
    ndvi_y = models.FloatField()
    gndvi = models.FloatField()
    rvi_1 = models.FloatField()
    gci = models.FloatField()
    rgvi = models.FloatField()
    dvi = models.FloatField()
    savi = models.FloatField()
    msavi = models.FloatField()
    osavi = models.FloatField()
    rdvi = models.FloatField()
    tvi = models.FloatField()
    tsavi = models.FloatField()
    pvi = models.FloatField()
    savi_2 = models.FloatField()
    atsavi = models.FloatField()
    ndwi = models.FloatField()
    npci = models.FloatField()
    srpi = models.FloatField()
    rvi_2 = models.FloatField()
    mcari = models.FloatField()
    mcari_1 = models.FloatField()
    mcari_2 = models.FloatField()
    mtvi_1 = models.FloatField()
    mtvi_2 = models.FloatField()
    r_mcari_mtvi_2 = models.FloatField()
    evi = models.FloatField()
    datt = models.FloatField()
    ndci = models.FloatField()
    psri = models.FloatField()
    sipi = models.FloatField()
    spvi = models.FloatField()
    tcari = models.FloatField()
    r_tcari_osavi = models.FloatField()
    reri = models.FloatField()
    ndre = models.FloatField()
    mtci = models.FloatField()
    evi_2 = models.FloatField()
    reci = models.FloatField()
    nexg = models.FloatField()
    ngrdi = models.FloatField()
    endvi = models.FloatField()
    ari_2 = models.FloatField()
    cri_2 = models.FloatField()
    nrvi = models.FloatField()
    osavi_2 = models.FloatField()
    evi_3 = models.FloatField()
    mevi = models.FloatField()
    vari = models.FloatField()
    tvi_2 = models.FloatField()
    mcari_osavi = models.FloatField()
    tcari_osavi = models.FloatField()
    wdrvi = models.FloatField()

    def __str__(self):
        return f'{self.plot.field_component.name} - Plot {self.plot.plot_number} - {self.var}'


class EdgeStateMachineStatus(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='edge_state_machine_statuses')
    status = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'Edge SM Status for Mission {self.mission.pk} - {self.status}'

class CloudStateMachineStatus(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='cloud_state_machine_statuses')
    status = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'Cloud SM Status for Mission {self.mission.pk} - {self.status}'

class DroneStatus(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='drone_status')
    timestamp = models.DateTimeField(default=datetime.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    battery_percentage = models.FloatField()
    speed = models.FloatField()
    mission_duration = models.DurationField()

    def __str__(self):
        return f'Drone Status for Mission {self.mission.pk} at {self.timestamp}'

