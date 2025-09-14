# Django Portfolio Website

A dynamic portfolio website built with Django, converted from static HTML/CSS/JavaScript.

## Features

- **Dynamic Content Management**: Easily update your personal information, skills, projects, and experience through Django Admin
- **Responsive Design**: Maintains the original responsive design with modern styling
- **Contact Form**: Functional contact form that saves messages to the database
- **Project Portfolio**: Showcase your projects with descriptions, technologies used, and links
- **Skills Section**: Display your technical skills with proficiency levels
- **Admin Interface**: User-friendly admin panel for content management

## Project Structure

```
portfolio_project/
├── portfolio/                 # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # URL patterns
│   ├── admin.py              # Admin configuration
│   └── migrations/           # Database migrations
├── templates/                # HTML templates
│   ├── base.html             # Base template
│   └── portfolio/            # App-specific templates
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── media/                    # User-uploaded files
├── portfolio_project/        # Django project settings
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

## Models

- **PersonalInfo**: Your basic information, contact details, and social media links
- **Skill**: Technical skills with proficiency levels and descriptions
- **Project**: Portfolio projects with technologies, descriptions, and links
- **ContactMessage**: Messages sent through the contact form
- **Experience**: Work experience, education, and certifications

## Getting Started

1. **Activate Virtual Environment**:
   ```bash
   portfolio_venv\Scripts\activate  # Windows
   source portfolio_venv/bin/activate  # macOS/Linux
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create Initial Data** (already done):
   ```bash
   python setup_data.py
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver 8080
   ```

6. **Access Admin Panel**:
   - URL: http://127.0.0.1:8080/admin/
   - Username: admin
   - Password: admin123

## Interactive Demos

The portfolio includes three fully functional interactive demos:

### 🧮 **Scientific Calculator** (http://127.0.0.1:8080/projects/calculator-demo/)
- Advanced mathematical operations (sin, cos, tan, log, ln, sqrt, power)
- Memory functions and calculation history
- Keyboard support for quick input
- Beautiful gradient design with animations
- Error handling and validation

### 🌤 **Weather App** (http://127.0.0.1:8080/projects/weather-demo/)
- Real-time weather data from OpenWeatherMap API
- Current conditions, temperature, humidity, pressure
- Weather icons and descriptions
- Loading states and error handling
- Responsive design for all devices

### ✅ **Python To Do List** (http://127.0.0.1:8080/projects/todo-demo/)
- Add, edit, and delete tasks
- Mark tasks as complete/incomplete
- Task counter (total, pending, completed)
- Keyboard shortcuts (Enter to add)
- Local storage persistence

## Authentication System

The portfolio includes a complete authentication system with user management:

### 🔐 **Login Page** (http://127.0.0.1:8080/login/)
- Secure user authentication
- Beautiful responsive design with animations
- Demo credentials provided for testing
- Redirect to dashboard after successful login
- Error handling for invalid credentials

### 📊 **Dashboard** (http://127.0.0.1:8080/dashboard/) - *Login Required*
- Portfolio statistics (projects, skills, messages)
- Recent projects overview
- Contact message management
- Quick action buttons for admin tasks
- Direct links to Django admin panel

### 🚀 **Registration** (http://127.0.0.1:8080/register/)
- User account creation
- Form validation and error handling
- Password strength requirements
- Automatic redirect to login after registration

### Key Authentication Features:
- **Protected Routes**: Dashboard requires authentication
- **Session Management**: Secure login/logout functionality
- **User Context**: Personalized welcome messages
- **Admin Integration**: Direct links to Django admin panel
- **Responsive Design**: Mobile-friendly authentication forms

## Customization

### Adding Content
1. Access the admin panel at `/admin/`
2. Add your personal information, skills, and projects
3. Upload images for projects and profile picture
4. Customize social media links and contact information

### Styling
- Main CSS file: `static/css/style.css`
- Dark mode functionality: `static/js/dark-mode.js`
- Templates can be customized in the `templates/` directory

### Deployment
For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure proper `ALLOWED_HOSTS`
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Use a production WSGI server like Gunicorn

## Original Static Files
The original static portfolio files are preserved in the `Webportfolio/` directory for reference.

## Features Converted from Static to Dynamic

✅ Personal information management
✅ Skills showcase with proficiency levels
✅ Contact form with database storage
✅ Responsive design preservation
✅ Dark mode functionality
✅ Social media links
✅ Project portfolio system
✅ Admin interface for content management

## Next Steps

- Add more projects through the admin panel
- Upload a profile picture
- Customize the styling to match your preferences
- Add more sections like testimonials or blog posts
- Deploy to a hosting platform like Heroku, DigitalOcean, or AWS