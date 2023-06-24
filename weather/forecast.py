from .weather_api import WeatherAPI
from .utils import format_temperature, format_datetime

class Forecast:
    def __init__(self, location):
        self.weather_api = WeatherAPI(location)

    def display_basic_forecast(self):
        """
        Display the basic weather forecast.
        """
        current_weather = self.weather_api.get_current_weather()

        if "error" in current_weather:
            print("Error:", current_weather["error"])
        else:
            location = current_weather["name"]
            temperature = current_weather["main"]["temp"]
            weather_condition = current_weather["weather"][0]["description"]

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {location}")
            print("Date:", format_datetime(current_weather["dt"]))
            print("Temperature:", format_temperature(temperature))
            print("Weather Condition:", weather_condition)

    def display_detailed_forecast(self):
        """
        Display the detailed weather forecast.
        """
        current_weather = self.weather_api.get_current_weather()

        if "error" in current_weather:
            print("Error:", current_weather["error"])
        else:
            location = current_weather["name"]
            temperature = current_weather["main"]["temp"]
            weather_condition = current_weather["weather"][0]["description"]
            humidity = current_weather["main"]["humidity"]
            wind_speed = current_weather["wind"]["speed"]
            precipitation = current_weather.get("rain", {}).get("1h", 0)
            uv_index = current_weather.get("uv_index", "N/A")
            sunrise = current_weather["sys"]["sunrise"]
            sunset = current_weather["sys"]["sunset"]

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {location}")
            print("Date:", format_datetime(current_weather["dt"]))
            print("Temperature:", format_temperature(temperature))
            print("Weather Condition:", weather_condition)
            print("Humidity:", humidity, "%")
            print("Wind Speed:", wind_speed, "km/h")
            print("Precipitation:", precipitation, "mm")
            print("UV Index:", uv_index)
            print("Sunrise Time:", format_datetime(sunrise))
            print("Sunset Time:", format_datetime(sunset))

    def display_forecast_for_multiple_days(self, days):
        """
        Display the weather forecast for multiple days.
        """
        forecast = self.weather_api.get_three_hour_forecast(days)

        if "error" in forecast:
            print("Error:", forecast["error"])
        else:
            location = forecast["city"]["name"]

            print("----------------------------------------")
            print("    WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {location}")

            for item in forecast["list"]:
                date = format_datetime(item["dt"])
                temperature = item["main"]["temp"]
                weather_condition = item["weather"][0]["description"]

                print("\nDate:", date)
                print("Temperature:", format_temperature(temperature))
                print("Weather Condition:", weather_condition)

    def display_hourly_forecast(self):
        """
        Display the hourly weather forecast.
        """
        forecast = self.weather_api.get_three_hour_forecast()

        if "error" in forecast:
            print("Error:", forecast["error"])
        else:
            location = forecast["city"]["name"]

            print("----------------------------------------")
            print("    HOURLY WEATHER FORECAST")
            print("----------------------------------------")
            print(f"Location: {location}")
            print("Date:", format_datetime(forecast["list"][0]["dt"]))

            for item in forecast["list"]:
                hour = format_datetime(item["dt"], format="%H:%M")
                temperature = item["main"]["temp"]
                weather_condition = item["weather"][0]["description"]

                print(f"\nHour: {hour}")
                print("Temperature:", format_temperature(temperature))
                print("Weather Condition:", weather_condition)
