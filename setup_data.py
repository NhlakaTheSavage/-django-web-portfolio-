#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio.models import PersonalInfo, Skill

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created: admin/admin123")

# Create sample personal info
if not PersonalInfo.objects.exists():
    personal_info = PersonalInfo.objects.create(
        name="Nicholas Dlomo",
        tagline="Web Developer | Problem Solver | Lifelong Learner",
        bio="Hi! I'm Nicholas Dlomo, a passionate web developer with a strong foundation in HTML, CSS, and JavaScript. I enjoy creating clean, responsive, and user-friendly websites that solve real-world problems. My goal is to continuously learn and grow as a developer, staying up-to-date with the latest technologies.",
        email="nicholasdlomo@gmail.com",
        phone="+27 78 993 6173",
        location="232 Mosetla Street, Atteridgeville, Pretoria, South Africa",
        linkedin_url="https://linkedin.com/in/dlomo-nicholas-684028348",
        github_url="https://www.github.com/NhlakaTheSavage",
        instagram_url="https://www.instagram.com/nhlaka_the_savage",
        youtube_url="https://youtube.com/@DlomoNicholas"
    )
    print("Personal info created")

# Create sample skills
skills_data = [
    {
        'name': 'HTML',
        'description': 'Proficient in structuring web pages with semantic HTML.',
        'icon_svg': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 7v10c0 5.55 3.84 9.74 9 11 5.16-1.26 9-5.45 9-11V7l-10-5z" fill="#E34F26"/></svg>',
        'proficiency_level': 3,
        'order': 1
    },
    {
        'name': 'CSS',
        'description': 'Expertise in styling and designing responsive layouts.',
        'icon_svg': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 7v10c0 5.55 3.84 9.74 9 11 5.16-1.26 9-5.45 9-11V7l-10-5z" fill="#1572B6"/></svg>',
        'proficiency_level': 3,
        'order': 2
    },
    {
        'name': 'JavaScript',
        'description': 'Comfortable with ES6+, DOM manipulation, async programming, and building interactive web applications.',
        'icon_svg': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 7v10c0 5.55 3.84 9.74 9 11 5.16-1.26 9-5.45 9-11V7l-10-5z" fill="#F7DF1E"/></svg>',
        'proficiency_level': 2,
        'order': 3
    },
    {
        'name': 'Python',
        'description': 'Experience with Python for web development, automation, and building scalable backend applications.',
        'icon_svg': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 7v10c0 5.55 3.84 9.74 9 11 5.16-1.26 9-5.45 9-11V7l-10-5z" fill="#3776AB"/></svg>',
        'proficiency_level': 2,
        'order': 4
    }
]

for skill_data in skills_data:
    if not Skill.objects.filter(name=skill_data['name']).exists():
        Skill.objects.create(**skill_data)
        print(f"Skill created: {skill_data['name']}")

print("Setup complete!")