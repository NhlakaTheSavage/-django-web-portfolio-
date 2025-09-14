#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project

# Update the Python To Do List project demo link
try:
    todo_project = Project.objects.get(title='Python To Do List')
    todo_project.demo_link = '/projects/todo-demo/'
    todo_project.save()
    print("Updated Python To Do List demo link!")
except Project.DoesNotExist:
    print("Python To Do List project not found!")