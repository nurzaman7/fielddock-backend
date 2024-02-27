# admin_site/forms.py

from django import forms
from .models import FieldComponent

class FieldDockForm(forms.ModelForm):
    class Meta:
        model = FieldComponent
        fields = ['name', 'description', 'address']

