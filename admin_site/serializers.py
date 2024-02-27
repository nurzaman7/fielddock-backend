# admin_site/serializers.py
from rest_framework import serializers
from .models import FieldComponent

class FieldComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldComponent
        fields = ['name']
