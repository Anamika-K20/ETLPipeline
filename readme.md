# Ecommerce ETL Pipeline

This project demonstrates a complete end-to-end ETL pipeline built with Python, Apache Airflow, and PostgreSQL. It extracts product data from the FakeStore API, transforms it with Pandas, and loads the final dataset into a PostgreSQL table.

## Overview

The pipeline follows a simple production-style flow:

FakeStore API -> Python Extract Script -> Pandas Transformation -> PostgreSQL Database -> Apache Airflow DAG

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Apache Airflow
- REST API from FakeStore

## Dataset Source

Product data is fetched from:

https://fakestoreapi.com/products

## Pipeline Steps

### 1. Extract

- Used the FakeStore API as the data source
- Fetched product data using Python `requests`
- Created an extraction function in Python
- Pulled JSON data from the API

### 2. Transform

- Converted JSON into a Pandas DataFrame
- Cleaned and structured the data
- Added a derived column:

```python
price_with_tax = price * 1.18
```

### 3. Load

- Used a SQLAlchemy engine
- Loaded the transformed data into PostgreSQL
- Stored the final output in the `products` table

## Issues Faced and Fixes

### PostgreSQL command confusion

Trying to run this directly in the terminal caused an error:

```sql
CREATE DATABASE ecommerce_db;
```

That is SQL, not a terminal command. The correct flow is to open `psql` first, then run SQL inside the PostgreSQL shell.

### Airflow CLI confusion

The older `airflow db init` command no longer applies in Airflow v3. The correct command is:

```bash
airflow db migrate
```

### DAG not visible initially

The DAG was not visible right away because it was paused or not loaded correctly. Refreshing the UI and checking the DAG list helped confirm it was available.

### Load task failure

An error appeared because the PostgreSQL table schema did not match the transformed dataset:

```text
column "description" does not exist
```

This was resolved by replacing the table instead of appending to it:

```python
if_exists="replace"
```

## Alternative Paths

### Manual SQL schema

Instead of letting Pandas create the table, you could define the schema manually:

```sql
CREATE TABLE products (
	id INT,
	title TEXT,
	price FLOAT,
	description TEXT,
	category TEXT,
	image TEXT,
	rating TEXT,
	price_with_tax FLOAT
);
```

This is more controlled and production-friendly, but it takes more effort.

### Airflow Connections

Instead of hardcoding credentials like `postgresql://postgres@localhost`, a better practice is to store database credentials in Airflow Connections through the Airflow Admin UI.

### Docker setup

You could also run Airflow and PostgreSQL in Docker containers for a more reproducible setup.

### Streaming pipeline

For an advanced version, the pipeline could be extended into a streaming architecture using Kafka and real-time processing.

## How to Run

### Start Airflow

```bash
airflow scheduler
airflow webserver
```

### Trigger the DAG

1. Open `http://localhost:8080`
2. Enable the DAG
3. Trigger it manually

## Output

The loaded data is stored in the PostgreSQL table:

```text
products
```

Columns:

- id
- title
- price
- description
- category
- image
- rating
- price_with_tax

## Key Learnings

- Building ETL pipelines with Python
- Working with REST APIs
- Transforming data with Pandas
- Loading data with SQLAlchemy
- Orchestrating workflows with Apache Airflow
- Debugging schema mismatch issues

## Future Improvements

- Add Docker support
- Use Airflow Connections for database credentials
- Add logging and retries
- Add a data validation layer
- Schedule the DAG for daily runs

## Final Summary

This project reflects real-world data engineering work: environment setup issues, Airflow CLI version differences, DAG orchestration problems, schema mismatches, and pipeline debugging. These are the kinds of problems that appear in production data workflows.
