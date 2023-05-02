import requests

class OpenWeatherMapWrapper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city):
        endpoint = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "imperial"
        }
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            data = response.json()
            weather = {
                "description": data["weather"][0]["description"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather
        else:
            raise Exception(f"Failed to get weather data for {city}: {response.content}")
