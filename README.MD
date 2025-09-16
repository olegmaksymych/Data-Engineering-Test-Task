# Mini Data Pipeline (Pre-Internship Test Task)

## 📌 Project Description
This project implements a simple ETL (Extract–Transform–Load) pipeline with Python, PostgreSQL, and Airflow.

**Data Flow:**
`API → Raw JSON → Cleaned CSV → PostgreSQL → SQL Analytics → Report`

---

## 🔧 Technologies
- Python 3.10+
- requests
- pandas
- pyarrow / fastparquet
- SQLAlchemy
- SQLite
- Docker / docker-compose
- Apache Airflow


## The security veriables
the security variables are saved in the .env file 
using load_dotenv() function from dotenv module
---

## 🚀 Steps Implemented

### 1. Extract
- API used: **[Visual Crossing API](https://www.visualcrossing.com/)** (no API key required).
- Data saved in local structure:
data/raw/response.json


### 2. Transform
- Loads raw JSON data from data/raw/response.json.
- Extracts only required fields:
    date, temp_max, temp_min, temp_avg, feelslike, precipitation types.
- Cleans data by skipping rows with missing temperatures.
- Adds a new column be_precipitation:
1) "was_rain" if rain was present
2) "was_snow" if snow was present
3) "no" if no precipitation
- Saves the processed data in CSV format:
data/processed/YYYY-MM-DD/data.csv


### 3. Load
- Loaded cleaned data into **PostgreSQL** (`local.db`) using **psycopg2**.
- Table: `weather`.

### 4. Analytics
- SQL queries:
- Average temperature
- Count of total records
- Average temperature grouped by hour
- Exported to:
data/report/report.json

---

## ▶️ How to Run
### **Local Run**
```bash
pip install -r requirements.txt
python src/main.py
```
ALSO - it is possible to run main.py using docker 
 **_docker-compose up -d --build_**     

### **_🧪Testing_**
Run tests regarding:
- Extracting data from API
- connection to PostgreSQL
- Transforming and Loading files 

### 📂 _**Outputs**_
data/raw/.../response.json → raw API response
data/processed/.../data.csv → processed data
PostgreSQL table weather → cleaned data in DB
data/reports/report.json → analytics report

### 📸  **_Screenshots Required_**
Raw file saved locally - picture 1
Processed csv - picture 1
Generated report - 1
PostgreSQL table with rows - picture 2 