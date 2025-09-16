import os
import pandas as pd
from dotenv import load_dotenv
from src.transform import transform_weather_data

def test_transform_weather_data():
    """ Tests the transformation of raw JSON data into CSV """
    try:
        load_dotenv()
        raw_file = os.getenv("PATH_TO_RAW_FILE")

        csv_file = transform_weather_data(raw_file)

        # Checking: file exists
        assert os.path.exists(csv_file), f"CSV file {csv_file} does not exist!"

        # Checking: the file is not empty
        df = pd.read_csv(csv_file)
        assert not df.empty, "CSV file is empty!"

        # Check: columns are needed
        expected_columns = {"date", "temp_max", "temp_min", "temp_avg", "feelslike", "be_precipitation"}
        missing_cols = expected_columns - set(df.columns)
        assert not missing_cols, f"Missing columns: {missing_cols}"

        # Check: be_precipitation has only correct values
        assert df['be_precipitation'].isin(["was_rain", "was_snow", "no"]).all(), \
            "Column 'be_precipitation' contains invalid values"

        print("Transform test passed successfully.")

    except Exception as e:
        print(f"Transform test failed: {e}")

if __name__ == "__main__":
    test_transform_weather_data()
