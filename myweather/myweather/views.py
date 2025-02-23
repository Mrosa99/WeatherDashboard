import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv, dotenv_values

load_dotenv()


def index(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.POST.get("city")

        api_key = os.getenv("API_KEY")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            print(weather_data)
        else:
            error_message = "City not found or API issue."

    return render(
        request,
        "index.html",
        {"weather_data": weather_data, "error_message": error_message},
    )
