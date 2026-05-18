import requests
import pandas as pd

url = "https://fakestoreapi.com/products"

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
df.to_csv("/Users/anamikakumari/ETL Pipeline/output/api_products.csv", index=False)
print("API data extracted successfully!")