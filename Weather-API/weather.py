import requests

# Create an Account -> find the API key.
API_KEY = "###################################"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# Retrieve some information.
response = requests.get(requests_url)
if response.status_code == 200:
    data = response.json()

    weather = data["weather"][0]["description"]
    print(f"Weather: {weather}")
    temperature = data["main"]["temp"]
    print(f"Temperature: {temperature}")
else:
    {}
