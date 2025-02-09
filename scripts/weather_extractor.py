import requests
from datetime import datetime
from config.config import OPENWEATHERMAP_API_KEY

def fetch_weather_data(city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['cod'] == 200:
        return {
            "city": city,
            "timestamp": datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            "temperature": data['main']['temp'],
            "weather": data['weather'][0]['description']
        }
    else:
        raise Exception("API error: " + data.get("message", "Unknown error"))

if __name__ == "__main__":
    weather_info = fetch_weather_data("Ho Chi Minh")
    print(weather_info)
