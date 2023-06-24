import os
import requests
from dotenv import load_dotenv
load_dotenv()

class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/"

    def __init__(self, location):
        self.location = location
        self.api_key = os.getenv("OPEN_WEATHER_MAP_API_KEY")

    def get_current_weather(self):
        """
        Fetch and return current weather data for the specified location.
        """
        try:
            endpoint = f"{self.BASE_URL}weather"
            params = {
                "q": self.location,
                "appid": self.api_key,
                "units": "metric"  # Use metric units (Celsius)
            }
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_three_hour_forecast(self, days=1):
        """
        Fetch and return 3-hour weather forecast for the specified location and number of days.
        """
        # Validate and adjust the number of days
        days = self.validate_and_adjust_days(days)
        
        # Calculate the number of time slots (each slot is 3 hours)
        time_slots = days * 8
        
        try:
            endpoint = f"{self.BASE_URL}forecast"
            params = {
                "q": self.location,
                "appid": self.api_key,
                "units": "metric",  # Use metric units (Celsius)
                "cnt": time_slots
            }
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def validate_and_adjust_days(self, days):
        """
        Validate the number of days for the forecast. If it exceeds 5, adjust it to 5.
        """
        if days < 1:
            return 1
        elif days > 5:
            print("Note: The forecast can only be retrieved for up to 5 days. Adjusting to 5 days.")
            return 5
        else:
            return days
