# Travel Booking Web Application

## Project Description
This is a Django-based travel booking web application using SQL database. The application allows users to register, log in,logout, view travel options, book tickets, and manage their bookings.

## Features
- User authentication (Register, Login, Logout)
- Browse available travel options
- Book travel tickets
- View and manage bookings
- Cancel bookings

## Prerequisites
Ensure you have the following installed:
- Python 3.12+
- Git
- SQLITE,MYSQL or any SQL-compatible database

## Setup Instructions
### 1. Clone the Repository
```bash
git https://github.com/Sivabokam7482/travel_booking
cd travel_book
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
Update `settings.py` with your database connection details:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.
## Contributing
Feel free to fork the repository and submit pull requests.
