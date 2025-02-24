import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


def index(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city_state = request.POST.get("city-state")
        if city_state:
            city_state_parts = city_state.split(",")
            if len(city_state_parts) == 2:
                city = city_state_parts[0].strip()
                state = city_state_parts[1].strip()

                api_key = os.getenv("API_KEY")
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=imperial"

                response = requests.get(url)

                if response.status_code == 200:
                    weather_data = response.json()
                else:
                    error_message = "City not found or API issue."
            else:
                error_message = (
                    "Please enter the city and state in 'City, State' format."
                )

    return render(
        request,
        "index.html",
        {"weather_data": weather_data, "error_message": error_message},
    )
