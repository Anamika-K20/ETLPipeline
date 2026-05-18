import pandas as pd
#read extracted API data
df = pd.read_csv("/Users/anamikakumari/ETL Pipeline/output/api_products.csv")
print("Original Data:")
print(df.head())

#Remove duplicates
df=df.drop_duplicates()

#Handle missing values
df=df.fillna("Unknown")

#Create a new column
df["price_with_tax"]=df["price"]*1.18

# Convert price column to float
df["price"] = df["price"].astype(float)

# Keep only important columns
df = df[["id", "title", "price", "price_with_tax", "category"]]

print("\nTransformed Data:")
print(df.head())

# Save transformed data
df.to_csv("/Users/anamikakumari/ETL Pipeline/output/transformed_products.csv", index=False)

print("\nTransformation completed successfully!")
