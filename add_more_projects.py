#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project, Skill

# Get skills
html_skill = Skill.objects.get(name='HTML')
css_skill = Skill.objects.get(name='CSS')
js_skill = Skill.objects.get(name='JavaScript')
python_skill = Skill.objects.get(name='Python')

# Add Weather App project
if not Project.objects.filter(title='Weather App').exists():
    weather_project = Project.objects.create(
        title='Weather App',
        short_description='A responsive weather application that provides real-time weather information.',
        description='''A dynamic weather application that fetches real-time weather data and displays it in a clean, user-friendly interface.

Features include:
- Current weather conditions for any city
- 5-day weather forecast
- Temperature in Celsius and Fahrenheit
- Weather icons and descriptions
- Responsive design for all devices
- Clean and intuitive user interface

Built using modern web technologies with API integration for accurate weather data.''',
        demo_link='Weather App/index.html',
        github_link='https://github.com/NhlakaTheSavage/weather-app',
        featured=True,
        order=2
    )
    weather_project.technologies.add(html_skill, css_skill, js_skill)
    print("Weather App project added!")

# Add Scientific Calculator project
if not Project.objects.filter(title='Scientific Calculator').exists():
    calc_project = Project.objects.create(
        title='Scientific Calculator',
        short_description='A fully functional scientific calculator with advanced mathematical operations.',
        description='''A comprehensive scientific calculator application that performs basic and advanced mathematical operations.

Features include:
- Basic arithmetic operations (+, -, ×, ÷)
- Scientific functions (sin, cos, tan, log, etc.)
- Memory functions (store, recall, clear)
- Parentheses support for complex calculations
- Error handling and validation
- Responsive design for desktop and mobile
- Clean and intuitive interface

Perfect for students, engineers, and anyone needing advanced calculation capabilities.''',
        demo_link='scientific/scientificCulculator.html',
        github_link='https://github.com/NhlakaTheSavage/scientific-calculator',
        featured=False,
        order=3
    )
    calc_project.technologies.add(html_skill, css_skill, js_skill)
    print("Scientific Calculator project added!")

print("Additional projects added successfully!")