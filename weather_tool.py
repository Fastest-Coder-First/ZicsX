from datetime import datetime, timedelta
from weather.forecast import Forecast
from weather.cli_parser import parse_arguments

args = parse_arguments()

location = args.location
days = args.days
detailed = args.detailed
hourly = args.hourly

forecast = Forecast(location)

if detailed and days > 1:
    forecast.display_detailed_forecast_for_multiple_days(days)
elif detailed:
    forecast.display_detailed_forecast()
elif days > 1 and hourly:
    for i in range(days):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        print()
        print("############################################")
        print(f"Hourly Forecast for {date}")
        print("############################################")
        forecast.display_hourly_forecast(date)
else:
    if hourly:
        forecast.display_hourly_forecast()
    else:
        forecast.display_forecast_for_multiple_days(days)
