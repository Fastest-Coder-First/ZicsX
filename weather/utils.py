from datetime import datetime

def format_temperature(celsius):
    """
    Format temperature in Celsius to a string with the degree symbol and Fahrenheit equivalent.
    """
    try:
        fahrenheit = celsius * 9/5 + 32
        return f"{celsius}°C ({fahrenheit}°F)"
    except TypeError:
        return "N/A"

def format_datetime(timestamp, format="%Y-%m-%d %H:%M:%S"):
    """
    Format UNIX timestamp to a string using the specified format.
    """
    try:
        return datetime.utcfromtimestamp(timestamp).strftime(format)
    except ValueError:
        return "N/A"
