# 🌦️ Django Weather App

A simple Django-based weather web application that allows users to enter a city name and fetch real-time weather information such as temperature, wind speed, and weather description using the GoWeather API.

---

## 📋 Prerequisites

- Python 3.8 or higher  
- pip (Python package manager)  
- Terminal or Command Prompt  

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Install Python

- Download Python from [python.org](https://www.python.org/)
- During installation, **check** the option “Add Python to PATH”
- Verify installation:

```bash
python --version
🔹 Step 2: Set Up Virtual Environment
bash
Copy
Edit
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv env

# Activate the environment
# For Windows:
env\Scripts\activate

# For Mac/Linux:
source env/bin/activate
🔹 Step 3: Install Required Packages
bash
Copy
Edit
pip install django
pip install requests
🔹 Step 4: Create Django Project and App
bash
Copy
Edit
# Create Django project
django-admin startproject WeatherProject

# Move into project directory
cd WeatherProject

# Create Django app
python manage.py startapp MyWeatherApp
🔹 Step 5: Configure the Project
Edit WeatherProject/settings.py:

python
Copy
Edit
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MyWeatherApp',
]
Create the templates folder:

bash
Copy
Edit
mkdir -p MyWeatherApp/templates
🔹 Step 6: Add View Logic
Edit MyWeatherApp/views.py:

python
Copy
Edit
from django.shortcuts import render
import requests

def home(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        url = f'https://goweather.herokuapp.com/weather/{city}'
        response = requests.get(url)
        data = response.json()
        data['city'] = city
    return render(request, 'index.html', {'data': data})
🔹 Step 7: Add Templates
Create a file: MyWeatherApp/templates/index.html

html
Copy
Edit
<!DOCTYPE html>
<html>
<head>
    <title>Weather App</title>
</head>
<body>
    <h1>🌤️ Weather Checker</h1>
    <form method="POST">
        {% csrf_token %}
        <input type="text" name="city" placeholder="Enter City Name" required>
        <button type="submit">Search</button>
    </form>

    {% if data.city %}
        <h2>Weather in {{ data.city }}</h2>
        <p><strong>Temperature:</strong> {{ data.temperature }}</p>
        <p><strong>Wind:</strong> {{ data.wind }}</p>
        <p><strong>Description:</strong> {{ data.description }}</p>
    {% endif %}
</body>
</html>
🔹 Step 8: Configure URLs
MyWeatherApp/urls.py (Create this file)
python
Copy
Edit
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
WeatherProject/urls.py
python
Copy
Edit
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyWeatherApp.urls')),
]
🔹 Step 9: Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
🔹 Step 10: Run the Server
bash
Copy
Edit
python manage.py runserver
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:8000/
💡 Usage
Enter a city name in the search input.

Click "Search".

View the weather information including:

Temperature

Wind

Weather description

🌐 API Used
This app uses the GoWeather API to fetch real-time weather information.
✅ No API key or authentication required.
