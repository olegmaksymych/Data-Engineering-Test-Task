import os
from extract import fetch_weather_data
from transform import transform_weather_data
from load import load_csv_psycopg2

if __name__ == "__main__":
    raw_file = r"C:\Users\olegm\PycharmProjects\PythonProject\src\data\raw\response.json"

    # 1. Download from the API only if there is no local file yet
    if not os.path.exists(raw_file):
        print("🌍 Fetching data from API...")
        raw_file = fetch_weather_data("London", "2024-01-01", "2024-12-31")
    else:
        print(f"📂 Using cached file: {raw_file}")

    # 2: Transforming
    processed_file = transform_weather_data(raw_file)

    # 3. Upload to the database
    load_csv_psycopg2(processed_file)

    print("✅ ETL pipeline completed successfully!")

