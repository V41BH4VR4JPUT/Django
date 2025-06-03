# Django Starter Project 🛠️

This repository demonstrates a beginner-friendly **Django project setup** featuring a basic web application. It includes Django's standard directory structure, database configuration with SQLite, form handling, and an HTML template. Ideal for learning and experimenting with Django's core features.

---

## 📁 Project Structure

```
v41bh4vr4jput-django/
├── README.md                    # Project documentation
└── firstproject/
    ├── db.sqlite3               # SQLite database
    ├── manage.py                # Django management utility
    ├── firstapp/                # Core application
    │   ├── admin.py             # Admin interface configuration
    │   ├── apps.py              # App configuration
    │   ├── forms.py             # Django forms
    │   ├── models.py            # Data models
    │   ├── tests.py             # Unit tests
    │   ├── urls.py              # App-specific URL patterns
    │   ├── views.py             # Application logic
    │   ├── migrations/          # DB migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_reservation.py
    │   │   └── __init__.py
    │   └── templates/
    │       └── index.html       # HTML template
    └── firstproject/           # Project configuration
        ├── settings.py         # Project settings
        ├── urls.py             # Root URL configuration
        ├── wsgi.py             # WSGI entry point
        └── asgi.py             # ASGI entry point
```

---

## 🚀 Features

* ✅ SQLite database integration
* ✅ Django forms and models
* ✅ Template rendering with `index.html`
* ✅ Basic URL routing and views setup
* ✅ Migration support for model changes
* ✅ Admin panel registration

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/v41bh4vr4jput-django.git
cd v41bh4vr4jput-django/firstproject
```

### 2. Set Up the Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Then open in your browser:

```
http://127.0.0.1:8000/
```

---

## 📌 Notes

* Templates are stored under `firstapp/templates/`
* Models and forms are defined in `models.py` and `forms.py` respectively
* `index.html` serves as the home page for the app


