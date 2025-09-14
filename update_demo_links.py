#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project

# Update Weather App demo link
try:
    weather_project = Project.objects.get(title='Weather App')
    weather_project.demo_link = '/projects/weather-demo/'
    weather_project.save()
    print("Updated Weather App demo link!")
except Project.DoesNotExist:
    print("Weather App project not found!")

# Update Scientific Calculator demo link
try:
    calc_project = Project.objects.get(title='Scientific Calculator')
    calc_project.demo_link = '/projects/calculator-demo/'
    calc_project.save()
    print("Updated Scientific Calculator demo link!")
except Project.DoesNotExist:
    print("Scientific Calculator project not found!")

print("Demo links updated successfully!")