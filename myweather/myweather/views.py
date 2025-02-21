import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


def index(request):
    weather_data = None
    if request.method == "GET":
        print("Form submitted!")
        city = request.GET.get("city")
        print(f"City entered: {city}")
        api_key = os.getenv("API_KEY")
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )

        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            print(weather_data)

        else:
            weather_data = {"error": "City not found or API issue."}

    return render(request, "index.html", {"weather_data": weather_data})
