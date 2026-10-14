import requests
import sys
import argparse

def get_weather(lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon,
              "current_weather": True}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()["current_weather"]

def main() -> None:
  
    parser = argparse.ArgumentParser(description="provide lat and long")
    parser.add_argument("latitude", type=float)
    parser.add_argument("longitude", type=float)
    args = parser.parse_args()
    try:
        w = get_weather({args.latitude}, {args.longitude})
        print(f"Temp: {w['temperature']}°C, "
            f"Wind: {w['windspeed']} km/h")
    except requests.exceptions.RequestException as e: 
        print(f"Couldn't reach the weather service: {e}",
              file=sys.stderr)
        sys.exit(1)

    finally:
        print("done")

if __name__ == "__main__":
    main()
        
