import pandas as pd
from sqlalchemy import create_engine

# Load transformed data
df = pd.read_csv("/Users/anamikakumari/ETL Pipeline/output/transformed_products.csv")


engine = create_engine(
    "postgresql://postgres@localhost:5432/ecommerce_db"
)

# Load into table
df.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded into PostgreSQL successfully!")