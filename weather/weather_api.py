from datetime import datetime, timedelta
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/"

    def __init__(self, location):
        self.location = location
        self.api_key = os.getenv("OPEN_WEATHER_MAP_API_KEY")

    def get_current_weather(self):
        url = f"{self.BASE_URL}weather"
        params = {
            "q": self.location,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        return response.json()
    
    # Get hourly forecast of the date given (this date must be in the next 5 days)
    def get_hourly_forecast(self, date=None):
        if date is None:
            date = datetime.now()
        else:
            date = datetime.strptime(date, "%Y-%m-%d")
        url = f"{self.BASE_URL}forecast"
        params = {
            "q": self.location,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        forecast_data = response.json()

        hourly_forecast = []
        for item in forecast_data["list"]:
            forecast_date = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            if forecast_date.date() == date.date():
                hourly_forecast.append(item)

        return hourly_forecast

# Get daily forecast for the next n days get only one forcast perday at 12:00:00
    def get_daily_forecast(self, days):
        url = f"{self.BASE_URL}forecast"
        params = {
            "q": self.location,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        forecast_data = response.json()

        daily_forecast = []
        for item in forecast_data["list"]:
            if item["dt_txt"].split()[1] == "12:00:00":
                daily_forecast.append(item)

        return daily_forecast[:days]
    
    def get_location_timezone(self):
        lat = self.latitude
        lon = self.longitude
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()
        timezone = data["timezone"]

        return timezone
