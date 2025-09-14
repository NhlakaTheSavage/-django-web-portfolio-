# Django Web Portfolio

A modern, responsive web portfolio built with Django featuring interactive project demos, user authentication, and a dynamic admin interface.

## 🌟 Features

- **Responsive Design**: Modern, mobile-first design with smooth animations
- **Interactive Project Demos**: 
  - Python To Do List with local storage
  - Scientific Calculator with advanced operations
  - Weather App with real-time data
- **User Authentication**: Complete login/register system with protected dashboard
- **Admin Interface**: Django admin for easy content management
- **Contact Form**: Functional contact form with CSRF protection
- **Dynamic Content**: Database-driven content management

## 🚀 Live Demo

<!-- Add your deployment URL here when available -->
Visit the live portfolio: [Your Portfolio URL]

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development)
- **Styling**: Custom CSS with gradients and animations
- **Authentication**: Django's built-in authentication system

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-web-portfolio.git
   cd django-web-portfolio
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv portfolio_venv
   
   # On Windows
   portfolio_venv\Scripts\activate
   
   # On macOS/Linux
   source portfolio_venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load initial data (optional)**
   ```bash
   python setup_data.py
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Portfolio: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🎯 Usage

### Admin Interface
- Access `/admin/` to manage portfolio content
- Add/edit personal information, skills, projects, and experiences
- View contact form submissions

### Authentication
- **Login**: Access protected areas
- **Register**: Create new user accounts
- **Dashboard**: View portfolio statistics and user info

### Project Demos
- **To Do List**: `/projects/todo-demo/` - Full CRUD operations with local storage
- **Calculator**: `/projects/calculator-demo/` - Scientific calculator with history
- **Weather App**: `/projects/weather-demo/` - Real-time weather information

## 📁 Project Structure

```
django-web-portfolio/
│
├── portfolio/                 # Main Django app
│   ├── migrations/           # Database migrations
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # URL patterns
│   └── admin.py             # Admin configuration
│
├── portfolio_project/        # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
│
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── portfolio/          # Portfolio templates
│   │   ├── home.html       # Homepage
│   │   ├── projects.html   # Projects page
│   │   ├── auth/           # Authentication templates
│   │   └── demos/          # Project demos
│
├── static/                  # Static files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Images
│
├── requirements.txt         # Python dependencies
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## 🎨 Customization

### Adding New Projects
1. Add project data through Django admin
2. Create demo template in `templates/portfolio/demos/`
3. Add URL pattern in `portfolio/urls.py`
4. Update navigation if needed

### Styling
- Main styles: `static/css/style.css`
- Demo styles: Individual demo templates
- Responsive breakpoints configured for mobile-first design

### Content Management
- Personal info, skills, and projects managed through Django admin
- Contact form submissions stored in database
- User authentication with built-in Django system

## 🚦 Running Tests

```bash
python manage.py test
```

## 📝 Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🚀 Deployment

### Heroku Deployment
1. Install Heroku CLI
2. Create `Procfile`: `web: gunicorn portfolio_project.wsgi`
3. Update `requirements.txt` with production dependencies
4. Configure environment variables
5. Deploy: `git push heroku main`

### Other Platforms
- Configure `ALLOWED_HOSTS` in settings
- Set up static file serving
- Configure database (PostgreSQL recommended for production)
- Set environment variables

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django framework for the robust backend
- Modern CSS techniques for responsive design
- Open source community for inspiration

## 📞 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/django-web-portfolio](https://github.com/yourusername/django-web-portfolio)