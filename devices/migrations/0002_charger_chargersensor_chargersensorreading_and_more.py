# Generated by Django 4.2.7 on 2024-02-14 18:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0001_initial'),
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('field_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chargers', to='admin_site.fieldcomponent')),
            ],
        ),
        migrations.CreateModel(
            name='ChargerSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_type', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=100)),
                ('specifications', models.TextField(blank=True, null=True)),
                ('charger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='devices.charger')),
            ],
        ),
        migrations.CreateModel(
            name='ChargerSensorReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('value', models.FloatField()),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='devices.chargersensor')),
            ],
        ),
        migrations.CreateModel(
            name='ChargerLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('charger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='devices.charger')),
            ],
        ),
    ]