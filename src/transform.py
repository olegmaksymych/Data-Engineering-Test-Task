import os
import pandas as pd
import json

def transform_weather_data(raw_file_path: str) -> str:
    """
    Transforms raw JSON data:
    - Leaves only the required fields
    - Cleans up incorrect values
    - Adds a 'be_precipitation' column: was_rain / was_snow / no
    """
    with open(raw_file_path, "r") as f:
        raw_data = json.load(f)

    records = []
    for day in raw_data.get('days', []):
        temp_avg = day.get('temp')
        temp_max = day.get('tempmax')
        temp_min = day.get('tempmin')
        feelslike = day.get('feelslike')
        precip_types = day.get('preciptype', [])

        if temp_avg is None or temp_max is None or temp_min is None:
            continue

        precip_types = day.get("preciptype") or []

        # Determining precipitation
        if "rain" in precip_types:
            be_precipitation = "was_rain"
        elif "snow" in precip_types:
            be_precipitation = "was_snow"
        else:
            be_precipitation = "no"

        record = {
            "date": day["datetime"],
            "temp_max": temp_max,
            "temp_min": temp_min,
            "temp_avg": temp_avg,
            "feelslike": feelslike,
            "be_precipitation": be_precipitation
        }
        records.append(record)

    df = pd.DataFrame(records)


    processed_path = f"data/processed"
    os.makedirs(processed_path, exist_ok=True)

    csv_path = f"{processed_path}/data.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8")

    print(f"Processed data saved successfully at {csv_path}")
    return csv_path
