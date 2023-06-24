from datetime import datetime, timedelta
import pytz
from .weather_api import WeatherAPI
from .utils import format_temperature, format_datetime

class Forecast:
    def __init__(self, location):
        self.weather_api = WeatherAPI(location)

    def display_basic_forecast(self):
        try:
            weather_data = self.weather_api.get_current_weather()
            temperature = weather_data["main"]["temp"]
            weather_condition = weather_data["weather"][0]["description"]

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {self.weather_api.location}")
            print("Date: Today")
            print(f"Temperature: {format_temperature(temperature)}")
            print(f"Weather Condition: {weather_condition}")
        except Exception as e:
            print("Error occurred while fetching weather data:", str(e))

    def display_detailed_forecast(self):
        try:
            weather_data = self.weather_api.get_current_weather()
            temperature = weather_data["main"]["temp"]
            weather_condition = weather_data["weather"][0]["description"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            precipitation = weather_data.get("rain", {}).get("1h", 0)
            uv_index = weather_data.get("uvi", 0)
            sunrise_time = weather_data["sys"]["sunrise"]
            sunset_time = weather_data["sys"]["sunset"]

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {self.weather_api.location}")
            print("Date: Today")
            print(f"Temperature: {format_temperature(temperature)}")
            print(f"Weather Condition: {weather_condition}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} km/h")
            print(f"Precipitation: {precipitation} mm")
            print(f"UV Index: {uv_index}")
            print(f"Sunrise Time: {format_datetime(sunrise_time)}")
            print(f"Sunset Time: {format_datetime(sunset_time)}")
        except Exception as e:
            print("Error occurred while fetching weather data:", str(e))

    def display_forecast_for_multiple_days(self, days):
        try:
            daily_forecast = self.weather_api.get_daily_forecast(days)

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {self.weather_api.location}")

            for item in daily_forecast:
                date = item["dt_txt"].split()[0]
                temperature = item["main"]["temp"]
                weather_condition = item["weather"][0]["description"]

                print()
                print(f"Date: {date}")
                print(f"Temperature: {format_temperature(temperature)}")
                print(f"Weather Condition: {weather_condition}")
        except Exception as e:
            print("Error occurred while fetching weather data:", str(e))

    # display hourly forecast for the date given as parameter or none will the current date
    def display_hourly_forecast(self, date=None):
        try:
            hourly_forecast = self.weather_api.get_hourly_forecast(date)

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {self.weather_api.location}")

            for item in hourly_forecast:
                date = item["dt_txt"]
                temperature = item["main"]["temp"]
                weather_condition = item["weather"][0]["description"]

                print()
                print(f"Date: {date}")
                print(f"Temperature: {format_temperature(temperature)}")
                print(f"Weather Condition: {weather_condition}")
        except Exception as e:
            print("Error occurred while fetching weather data:", str(e))

    def display_detailed_forecast_for_multiple_days(self, days):
        try:
            daily_forecast = self.weather_api.get_daily_forecast(days)

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {self.weather_api.location}")

            for item in daily_forecast:
                date = item["dt_txt"].split()[0]
                temperature = item["main"]["temp"]
                weather_condition = item["weather"][0]["description"]
                humidity = item["main"]["humidity"]
                wind_speed = item["wind"]["speed"]
                precipitation = item.get("rain", {}).get("1h", 0)
                uv_index = item.get("uvi", 0)
                sunrise_time = item["sys"]["sunrise"]
                sunset_time = item["sys"]["sunset"]

                print()
                print(f"Date: {date}")
                print(f"Temperature: {format_temperature(temperature)}")
                print(f"Weather Condition: {weather_condition}")
                print(f"Humidity: {humidity}%")
                print(f"Wind Speed: {wind_speed} km/h")
                print(f"Precipitation: {precipitation} mm")
                print(f"UV Index: {uv_index}")
                print(f"Sunrise Time: {format_datetime(sunrise_time)}")
                print(f"Sunset Time: {format_datetime(sunset_time)}")
        except Exception as e:
            print("Error occurred while fetching weather data:", str(e))
