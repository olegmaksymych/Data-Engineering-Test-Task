import os
from src.extract import fetch_weather_data


def test_fetch_weather_data():
    """  Tests data loading from the API and checks for the existence of the file. """
    try:
        # Call the function
        file_path = fetch_weather_data(city="Lviv", start_date="2024-01-01", end_date="2024-01-03")

        # Checking: file exists
        assert os.path.exists(file_path), f"File {file_path} does not exist!"

        # Checking: file size > 0
        assert os.path.getsize(file_path) > 0, "File is empty!"

        print("Extract test passed successfully.")

    except Exception as e:
        print(f"Extract test failed: {e}")


if __name__ == "__main__":
    test_fetch_weather_data()
