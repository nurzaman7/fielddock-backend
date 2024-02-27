from django.db import models


class FieldComponent(models.Model):
    name = models.CharField(max_length=100, verbose_name='Field Name')
    description = models.TextField(verbose_name='Description')
    address = models.CharField(max_length=255, verbose_name='Address')


    def __str__(self):
        return self.name

