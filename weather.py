import requests

def get_weather(lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon,
              "current_weather": True}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()["current_weather"]