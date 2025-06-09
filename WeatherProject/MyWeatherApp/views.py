from django.shortcuts import render
import requests
import json

def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            # Using a different API that doesn't require authentication
            url = f"https://goweather.herokuapp.com/weather/{city}"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                context = {
                    "city": city,
                    "temp": data.get('temperature', 'N/A'),
                    "description": data.get('description', 'N/A'),
                    "wind_speed": data.get('wind', 'N/A'),
                    "forecast": data.get('forecast', [])
                }
            else:
                context = {"error": "City not found or API error"}
        except Exception as e:
            context = {"error": f"Error: {str(e)}"}
    else:
        context = {}
    return render(request, "index.html", context)