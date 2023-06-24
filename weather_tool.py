from weather.cli_parser import CliParser
from weather.forecast import Forecast

def main():
    # Parse command-line arguments
    cli_parser = CliParser()
    args = cli_parser.parse_arguments()

    # Validate command-line arguments
    cli_parser.validate_arguments(args)

    # Retrieve location from command-line arguments
    location = args.location

    # Initialize Forecast object
    forecast = Forecast(location)

    # Display weather forecast based on command-line options
    if args.detailed and args.days is not None and args.hourly:
        forecast.display_detailed_forecast_for_multiple_days_hourly(args.days)
    elif args.detailed and args.days is not None:
        forecast.display_detailed_forecast_for_multiple_days(args.days)
    elif args.hourly and args.days is not None:
        forecast.display_hourly_forecast_for_multiple_days(args.days)
    elif args.detailed and args.hourly:
        forecast.display_detailed_hourly_forecast()
    elif args.detailed:
        forecast.display_detailed_forecast()
    elif args.days is not None and args.hourly:
        forecast.display_hourly_forecast_for_multiple_days(args.days)
    elif args.days is not None:
        forecast.display_forecast_for_multiple_days(args.days)
    elif args.hourly:
        forecast.display_hourly_forecast()
    else:
        forecast.display_basic_forecast()

if __name__ == "__main__":
    main()
