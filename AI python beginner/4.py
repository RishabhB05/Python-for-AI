# Weather API Example
# Working with APIs
import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)


# With function
import requests
def get_weather(lat, lan):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lan}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data

paris_data= get_weather(48.85, 2.35)  # Paris coordinates
london_data = get_weather(51.51, -0.13)  # London coordinates
new_york_data = get_weather(40.71, -74.01)  # New York coordinates

print(paris_data)
print(london_data)
print(new_york_data)