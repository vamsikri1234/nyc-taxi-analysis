# Databricks notebook source
# MAGIC %md
# MAGIC ## Downloading Dataset ##

# COMMAND ----------

# https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet

# https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-01.parquet

# https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2024-01.parquet

# https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2024-02.parquet

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists nyc_cleansed

# COMMAND ----------

# MAGIC %run ../utility/read_write_util

# COMMAND ----------

import requests
from datetime import datetime


# Example: Get all months of 2024
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
base_dbfs = "/Volumes/workspace/nyc_cleansed/dataset/NYC/trip-data/"

files_urls = {

    "yellow" : [f"{base_url}yellow_tripdata_2024-{month:02}.parquet" for month in range(1,13)],
    "green" : [f"{base_url}green_tripdata_2024-{month:02}.parquet" for month in range(1,13)],
    "fhv" : [f"{base_url}fhv_tripdata_2024-{month:02}.parquet" for month in range(1,13)],
    "fhvhv" : [f"{base_url}fhvhv_tripdata_2024-{month:02}.parquet" for month in range(1,13)]

}

base_urls = {
    "yellow" : f"{base_dbfs}yellow/",
    "green" : f"{base_dbfs}green/",
    "fhv" : f"{base_dbfs}fhv/",
    "fhvhv" : f"{base_dbfs}fhvhv/"
}

for _file in files_urls:
    print(f"================================= Loading : {_file}=================================")
    for _file_url in files_urls[_file]:
        file_copy(_file_url , base_urls[_file] + _file_url.split('/')[-1]) 
    print(f"================================= Loaded : {_file}=================================")

# COMMAND ----------

data_sources = base_urls

data_sources

# COMMAND ----------

# Reading Data into DataFrames

read_options = {
    "header": "true",
    "inferSchema": "true"
}

for _data in data_sources:
    globals()[f"{_data}_taxi_df"] = read_data(source_file_path = data_sources[_data],
                                              source_file_format='parquet',
                                              read_options=read_options)
                                              


# COMMAND ----------

display(fhvhv_taxi_df)

# COMMAND ----------

# writing dataframe to table

for _data in data_sources:

    write_data(
        df = globals()[f"{_data}_taxi_df"],
        target_file_path = f"nyc_cleansed.{_data}_taxi",
        target_file_format='delta',
        mode_type='overwrite'
    
    )




# COMMAND ----------

# MAGIC %sql
# MAGIC select source_filename,count(1) from default.nyc_yellowtaxi 
# MAGIC group by 1
