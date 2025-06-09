# Django Weather App

A simple weather application built with Django that displays current weather conditions and forecasts for cities worldwide.

![Weather App Screenshot](screenshot.png)

## Live Demo
Check out the live demo: [Django Weather App](https://your-app-url.vercel.app)

## Features
- Search for weather by city name
- View current temperature and wind speed
- See weather description and conditions
- 3-day weather forecast
- Clean, responsive Bootstrap UI
- No API key required

## Tech Stack
- Django
- Python Requests
- Bootstrap 5
- GoWeather API

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/django-weather-app.git
cd django-weather-app

### Step 2: Set Up Virtual Environment
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv env

# Activate the environment
# For Windows:
env\Scripts\activate
# For Mac/Linux:
source env/bin/activate

pip install django requests

cd WeatherProject
python manage.py migrate

python manage.py runserver

WeatherProject/
├── MyWeatherApp/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   └── urls.py
├── WeatherProject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

