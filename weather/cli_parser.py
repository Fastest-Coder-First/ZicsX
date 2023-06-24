import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Weather Forecast Tool")
    parser.add_argument("--location", type=str, required=True, help="Location for weather forecast")
    parser.add_argument("--days", type=int, default=1, help="Number of days for weather forecast")
    parser.add_argument("--detailed", action="store_true", help="Display detailed weather forecast")
    parser.add_argument("--hourly", action="store_true", help="Display hourly weather forecast")
    return parser.parse_args()
