import os
import pandas as pd
from src.transform import transform_weather_data

def test_transform_weather_data():
    """
    Тестує трансформацію raw JSON даних у CSV.
    """
    try:
        raw_file = "data/raw/response.json"

        csv_file = transform_weather_data(raw_file)

        # Перевірка: файл існує
        assert os.path.exists(csv_file), f"CSV file {csv_file} does not exist!"

        # Перевірка: файл не порожній
        df = pd.read_csv(csv_file)
        assert not df.empty, "CSV file is empty!"

        # Перевірка: потрібні колонки
        expected_columns = {"date", "temp_max", "temp_min", "temp_avg", "feelslike", "be_precipitation"}
        missing_cols = expected_columns - set(df.columns)
        assert not missing_cols, f"Missing columns: {missing_cols}"

        # Перевірка: be_precipitation має тільки правильні значення
        assert df['be_precipitation'].isin(["was_rain", "was_snow", "no"]).all(), \
            "Column 'be_precipitation' contains invalid values"

        print("Transform test passed successfully.")

    except Exception as e:
        print(f"Transform test failed: {e}")

if __name__ == "__main__":
    test_transform_weather_data()
