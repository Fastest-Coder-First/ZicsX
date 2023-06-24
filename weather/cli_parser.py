import argparse

class CliParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Weather Forecasting Tool")

    def parse_arguments(self):
        self.parser.add_argument("--location", type=str, required=True, help="Location to retrieve the weather forecast for")
        self.parser.add_argument("--detailed", action="store_true", help="Display detailed weather information")
        self.parser.add_argument("--days", type=int, help="Retrieve weather forecasts for 'n' number of days")
        self.parser.add_argument("--hourly", action="store_true", help="Display hourly weather forecasts")
        return self.parser.parse_args()

    def validate_arguments(self, args):
        if args.days is not None and (args.days < 1 or args.days > 5):
            self.parser.error("The number of days for the forecast should be between 1 and 5.")
