import psycopg2

DB_USER = "postgres"
DB_PASSWORD = "password"
DB_NAME = "home_task"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ Successful connection to the database!")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print("PostgreSQL версія:", db_version)

    cur.close()
    conn.close()
    print("🔌 Connection closed.")

except Exception as e:
    print("❌ Connection error:", e)
