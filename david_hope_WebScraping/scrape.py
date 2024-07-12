import requests
import pandas as pd
import json

API_KEY = 'e98f93610d9bc275f33827065db583d4'
CITY = 'Nairobi'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Step 1: Sending an HTTP request to the OpenWeatherMap API
response = requests.get(URL)

# Checking if the request was successful
if response.status_code == 200:
    # Step 2: Parsing the JSON content
    data = response.json()
    
    # Step 3: Extracting relevant data
    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'weather': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }

    # Step 4: Printing the extracted data
    print(weather_data)

    # Step 5: Saveing data to a CSV file
    df = pd.DataFrame([weather_data])
    df.to_csv('weather_data.csv', index=False)

    # Step 6: Saving
    #  data to a JSON file
    with open('weather_data.json', 'w') as json_file:
        json.dump(weather_data, json_file, indent=4)

    print("Data successfully saved to weather_data.csv and weather_data.json")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
