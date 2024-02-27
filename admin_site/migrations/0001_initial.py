# Generated by Django 4.2.7 on 2023-12-08 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Field Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
            ],
        ),
    ]