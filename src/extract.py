import os
import requests
import json
from dotenv import load_dotenv


def fetch_weather_data(city: str, start_date: str, end_date: str) -> str:
    """
    Downloads weather data from the Visual Crossing API and saves it to the local folder /data/raw/yyyy-mm-dd/.
    Returns the path to the saved JSON file.
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in .env file")

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start_date}/{end_date}?unitGroup=metric&key={api_key}&include=days"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    data = response.json()
    raw_path = f"data/raw"
    os.makedirs(raw_path, exist_ok=True)

    file_path = f"{raw_path}/response.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Raw data saved successfully at {file_path}")
    return file_path

