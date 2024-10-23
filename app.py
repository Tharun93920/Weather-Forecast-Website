from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Constants
API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Home Route (Handles both GET and POST requests)
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None  # Default value

    if request.method == 'POST':
        city = request.form.get('city')  # Get the city from the form input
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # Build the API request URL
        response = requests.get(url)  # Make a request to the weather API

        if response.status_code == 200:  # Check if the request was successful
            weather_data = response.json()  # Parse the JSON response
        else:
            weather_data = None  # If city not found or API error

    # Render the HTML template with the weather data (if any)
    return render_template('index.html', weather=weather_data)

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

