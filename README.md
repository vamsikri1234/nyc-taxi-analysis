# 🗽 NYC Taxi Data Engineering Project – Databricks

This project is a **data engineering pipeline** for processing and managing **NYC Taxi trip data** using **Apache Spark on Databricks**. It includes building a scalable ETL pipeline, data quality checks, and performance optimizations with **Delta Lake** for downstream analytics.
It generates insights about taxi usage patterns, trip durations, fares, pickup/dropoff hotspots, and other factors affecting urban mobility
---

## 🧱 Project Goals

* Build robust, reusable data ingestion and transformation pipelines
* Use Delta Lake for scalable, ACID-compliant data storage
* Implement data quality checks and handle corrupt records
* Partition and optimize datasets for query performance
* Enable downstream analytics and reporting

---

## 🔧 Tech Stack

| Component       | Technology                        |
| --------------- | --------------------------------- |
| Platform        | Databricks (Community/Enterprise) |
| Language        | Python (PySpark)                  |
| Data Processing | Apache Spark                      |
| Storage Format  | Delta Lake                        |
| Scheduling      | Databricks Workflows / Jobs       |
| Orchestration   | Optional: Airflow / dbx           |
| Data Source     | NYC TLC Trip Records              |

---

## 📁 Project Structure

```
nyc-taxi-data-engineering/
│
├── notebooks/
│   ├── Bronze Layer/
|       └── DataIngest
│
├── configs/
│   └── 
│
├── workflows/
│   └── databricks_job_config.json
│
├── data/ 
│
├── README.md
```

---

## 🛠️ Pipeline Architecture

```
            +-------------+
            |  Raw Data   | (CSV/Parquet from TLC)
            +-------------+
                   |
                   ▼
         +-------------------+
         | Bronze Layer (Raw)|
         | - Basic ingestion |
         +-------------------+
                   |
                   ▼
        +------------------------+
        | Silver Layer (Cleaned) |
        | - Null handling        |
        | - Schema enforcement   |
        | - Type casting         |
        +------------------------+
                   |
                   ▼
     +----------------------------------+
     | Gold Layer (Aggregated / Final) |
     | - Summaries, KPIs, Aggregations |
     +----------------------------------+
```

---

## 🚀 Key Features

* ✅ Load TLC data from cloud storage or Databricks datasets
* ✅ Use **Auto Loader** for incremental file ingestion (optional)
* ✅ Schema inference with validation against expected types
* ✅ Write in **Delta Lake** format with partitioning (e.g., by year/month)
* ✅ Handle bad/corrupt records and log errors
* ✅ Perform aggregations for downstream BI/analytics use
* ✅ Schedule with Databricks Jobs or Workflows

---

## 💡 Example Transformations

* Convert pickup/dropoff timestamps to datetime
* Compute trip duration in minutes
* Filter out invalid coordinates and zero-distance trips
* Generate daily and monthly aggregates by zone
* Optimize tables with `ZORDER` and `OPTIMIZE`

---

## 📥 Sample Data Source

NYC TLC Public Dataset (Yellow Taxi):

```python
df = spark.read.format("parquet").load("/databricks-datasets/nyctaxi/tripdata/yellow/")
```

Or load from S3/ADLS:

```python
df = spark.read.csv("s3://my-bucket/nyc-taxi/yellow_tripdata_*.csv", header=True)
```

---

## ✅ Data Quality Checks

* Null value checks (pickup/dropoff datetime, fare, etc.)
* Range validation (e.g., positive fare amount, duration > 0)
* Schema mismatch alerts
* Duplicate row detection (based on `trip_id` or composite keys)

---

## 📆 Job Orchestration

Use **Databricks Workflows** or **Databricks Jobs** for orchestration. Example:

* Run ingestion daily or hourly
* Trigger cleaning after ingestion
* Schedule aggregation jobs weekly

---

## 📊 Outputs

* Delta Tables for each layer: `/delta/bronze/`, `/delta/silver/`, `/delta/gold/`
* Final gold tables ready for analytics in Databricks SQL or Power BI/Tableau
* Logs & audit records of corrupt/malformed data

---

## 🔮 Future Enhancements

* Add **MLflow** tracking for predictions (e.g., fare estimator)
* Integrate weather or traffic datasets
* Real-time streaming ingestion with **Auto Loader + Structured Streaming**
* Deployment using **dbx CLI** for CI/CD

---

## 👤 Author

*Vamsi Krishna*
\[LinkedIn / GitHub / Portfolio]

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

