# ELAYANE - Python and API Based Weather Forecast Application

Elayane Weather Forecast App is a visually appealing weather forecasting application developed using Python and Tkinter. It provides detailed weather data for any city, including current temperature, wind speed, humidity, pressure, and a 7-day forecast with sunrise, sunset, moonrise, moonset, and moon phase information. The app also includes graphical representations of temperature variations over time.

# Features
**Current Weather Information:**  Get current temperature, wind speed, humidity, and weather conditions for any city.
**7-Day Forecast:** Displays weather details for the next 7 days, including images of weather conditions, sunrise, sunset, moonrise, moonset, and moon phase data.
**Graphical Data Visualization:** Shows temperature variations over time with both line and bar charts for easy understanding.
**Timezone and Local Time Display:** Shows the city's timezone and local time.
**Visually Appealing Interface:** Customized with backgrounds, icons, and styles to make the app more engaging and user-friendly.

# How It Works
Input City Name: The user inputs the name of the city they want the weather information for.
Fetch Data: The app uses the OpenWeatherMap API to fetch weather data based on the city entered.
Display Data: It displays the weather data in a well-organized manner on the app's interface.
Graphical Representation: It also generates and displays line and bar charts showing the temperature changes over time.

# Prerequisites
Python 3.x
**Required Libraries:**
1) tkinter: For creating the GUI.
2) ttkthemes: For theming the app.
3) geopy: To get geographical information based on the city name.
4) timezonefinder: To fetch the timezone of the city.
5) requests: To send requests to the weather API.
6) pytz: For handling timezones.
7) Pillow (PIL): For handling images.
8) matplotlib: For plotting graphs.

# Installation
**Clone the Repository:**

**Install Required Libraries:**
pip install tkinter ttkthemes geopy timezonefinder requests pytz pillow matplotlib

**Run the Application:**
python elayane_weather_app.py

# API Key
To use the Elayane Weather Forecast App, you need an API key from OpenWeatherMap. Replace the placeholder YOUR_API_KEY in the code with your actual API key.

# Usage
1) Launch the application by running the Python script.
2) Enter the city name in the search bar.
3) Click the search icon or press Enter.
4) View the current weather details and the 7-day forecast.
5) Check the graphical representations of temperature variations.

# Screenshots
**Main Interface:** Shows the weather details and forecast with background images and icons.
**Graphical Representation:** Line and bar charts showing temperature variations over time.

# Error Handling
The app handles errors like incorrect city names or network issues by displaying user-friendly error messages.

# Contribution
Contributions are welcome! If you find any issues or have suggestions, please feel free to fork the repository, make changes, and submit a pull request.

