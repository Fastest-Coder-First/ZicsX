Weather Forecasting Tool

Weather Forecasting Tool
========================

Architectural Flow
------------------

This Weather Forecasting Tool follows a modular and component-based architecture. The main components are:

* Command-Line Interface (CLI): Handles user inputs and retrieves weather forecasts.
* OpenWeatherMap API Integration: Retrieves weather data from the OpenWeatherMap API.
* Data Parsing: Extracts relevant weather information from the API response.
* CLI Output: Displays the weather forecast to the user in the terminal.

CLI Commands
------------

To use the Weather Forecasting Tool, follow these command-line interface (CLI) commands with examples:

### Basic Weather Forecast

    python weather_tool.py --location "San Francisco"

Output:

    ----------------------------------------
        WEATHER FORECAST
    ----------------------------------------
    Location: San Francisco
    
    Date: 2023-06-24
    Temperature: 12.97°C (55.346000000000004°F)
    Weather Condition: broken clouds

### Detailed Weather Forecast

    python weather_tool.py --location "San Francisco" --detailed

Output:

    ----------------------------------------
        WEATHER FORECAST
    ----------------------------------------
    Location: San Francisco
    Date: Today
    Temperature: 12.96°C (55.328°F)
    Weather Condition: broken clouds
    Humidity: 85%
    Wind Speed: 6.71 km/h
    Precipitation: 0 mm
    UV Index: 0
    Sunrise Time: 2023-06-24 12:48:43
    Sunset Time: 2023-06-25 03:35:20

### Weather Forecast for Multiple Days

    python weather_tool.py --location "San Francisco" --days 3

Output:

    ----------------------------------------
        WEATHER FORECAST
    ----------------------------------------
    Location: San Francisco
    
    Date: 2023-06-24
    Temperature: 12.97°C (55.346000000000004°F)
    Weather Condition: broken clouds
    
    Date: 2023-06-25
    Temperature: 12.84°C (55.112°F)
    Weather Condition: overcast clouds
    
    Date: 2023-06-26
    Temperature: 12.96°C (55.328°F)
    Weather Condition: light rain

Environment Setup and CLI Execution
-----------------------------------

1. Clone the project repository.
2. Create a virtual environment:  
    `python -m venv myenv`
3. Activate the virtual environment:
    * For Windows:  
        `myenv\Scripts\activate`
    * For Linux/Mac:  
        `source myenv/bin/activate`
4. Install the required dependencies:  
    `pip install -r requirements.txt`
5. Run the CLI command:  
    `python weather_tool.py --location [location]`
