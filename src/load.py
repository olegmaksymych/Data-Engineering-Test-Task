
import os
import csv
import psycopg2
from dotenv import load_dotenv

def load_csv_psycopg2(csv_file_path: str):
    """Download CSV in PostgreSQL using psycopg2."""
    load_dotenv()
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = os.getenv("DB_NAME")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    try:
        # Connecting to the database
        conn = psycopg2.connect(
            dbname=db, user=user, password=password, host=host, port=port
        )
        cursor = conn.cursor()
        print("✅ Connected to PostgreSQL.")

        # Read CSV
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)  # first line - headers

            # Create a table (if necessary)
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS weather (
                {', '.join([f'{col} TEXT' for col in headers])}
            );
            """
            cursor.execute(create_table_query)
            print("📦 Table 'weather' ensured.")

            # Clearing the table (optional)
            cursor.execute("DELETE FROM weather;")

            # Loading strings
            for row in reader:
                insert_query = f"""
                INSERT INTO weather ({', '.join(headers)})
                VALUES ({', '.join(['%s'] * len(row))});
                """
                cursor.execute(insert_query, row)

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ CSV successfully loaded into the 'weather' table.")

    except Exception as e:
        print(f"❌ Error: {e}")
        raise

