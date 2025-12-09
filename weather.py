import requests
import sys

BASE_URL = "https://wttr.in"


def fetch_weather(location: str):
    """Fetch weather data for a location from wttr.in as JSON."""
    url = f"{BASE_URL}/{location}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: could not contact the weather service. ({e})")
        return None

    try:
        data = response.json()
    except ValueError:
        print("Error: received a response, but it was not valid JSON.")
        return None

    return data


def display_current(data: dict, location: str):
    """Print current weather conditions."""
    try:
        current = data["current_condition"][0]
    except (KeyError, IndexError, TypeError):
        print("Error: unexpected data format for current conditions.")
        return

    temp_c = current.get("temp_C")
    feels_c = current.get("FeelsLikeC")
    desc_list = current.get("weatherDesc", [])
    desc = desc_list[0]["value"] if desc_list else "No description"
    humidity = current.get("humidity")

    print(f"\nCurrent weather for {location}:")
    print(f"  {desc}")
    print(f"  Temperature: {temp_c}°C (feels like {feels_c}°C)")
    print(f"  Humidity: {humidity}%")


def display_forecast(data: dict, days: int = 3):
    """Print a simple multi-day forecast."""
    try:
        weather_days = data["weather"]
    except (KeyError, TypeError):
        print("Error: unexpected data format for forecast.")
        return

    print(f"\n{days}-day forecast:")
    for day in weather_days[:days]:
        date = day.get("date", "???")
        avg_temp = day.get("avgtempC", "?")
        max_temp = day.get("maxtempC", "?")
        min_temp = day.get("mintempC", "?")

        # Try to pick a mid-day description
        hourly = day.get("hourly", [])
        if len(hourly) >= 5:
            desc_list = hourly[4].get("weatherDesc", [])
        else:
            desc_list = []
        desc = desc_list[0]["value"] if desc_list else "No description"

        print(f"  {date}: {desc}, {min_temp}–{max_temp}°C (avg {avg_temp}°C)")


def main():
    print("=== Simple Weather Dashboard ===")
    print("Type 'q' to quit.\n")

    while True:
        location = input("Enter a city or location: ").strip()
        if location.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        if not location:
            print("Please enter a location name.")
            continue

        data = fetch_weather(location)
        if not data:
            # Error was already printed
            continue

        display_current(data, location)
        display_forecast(data, days=3)


if __name__ == "__main__":
    main()
