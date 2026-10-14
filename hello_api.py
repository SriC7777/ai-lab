import requests
import argparse

def get_weather(lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon,
              "current_weather": True}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()["current_weather"]

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("latitude")
        parser.add_argument("longitude")
        args = parser.parse_args()
        w = get_weather({args.latitude}, {args.longitude})
        print(f"Temp: {w['temperature']}°C, "
            f"Wind: {w['windspeed']} km/h")
    except (ValueError,TypeError) as e: 
        print(e)

    finally:
        print("done")
            
        
