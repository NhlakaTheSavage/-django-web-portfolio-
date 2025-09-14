#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project, Skill

# Get Python and JavaScript skills
python_skill = Skill.objects.get(name='Python')
html_skill = Skill.objects.get(name='HTML')
css_skill = Skill.objects.get(name='CSS')
js_skill = Skill.objects.get(name='JavaScript')

# Create Python To Do List project
if not Project.objects.filter(title='Python To Do List').exists():
    todo_project = Project.objects.create(
        title='Python To Do List',
        short_description='A dynamic task management application built with Python and web technologies.',
        description='''A comprehensive task management application that allows users to create, edit, delete, and organize their daily tasks. 
        
Features include:
- Add new tasks with descriptions and due dates
- Mark tasks as complete/incomplete
- Edit existing tasks
- Delete tasks
- Filter tasks by status (all, pending, completed)
- Responsive design for mobile and desktop
- Local storage persistence
        
Built using modern web technologies with a focus on user experience and clean, intuitive interface design.''',
        demo_link='http://127.0.0.1:8080/projects/todo-demo/',
        github_link='https://github.com/NhlakaTheSavage/python-todo-list',
        featured=True,
        order=1
    )
    
    # Add technologies used
    todo_project.technologies.add(python_skill, html_skill, css_skill, js_skill)
    
    print("Python To Do List project added successfully!")
else:
    print("Python To Do List project already exists!")