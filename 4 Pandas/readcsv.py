import pandas as pd

try:
    sales_data = pd.read_csv("C:/Users/ayush/Jupyter/sales_data.csv")
    print("✅ CSV file loaded successfully!")
    print(sales_data.head()) # top 5 records
    print("\n" , sales_data.tail())
    print("\n" , sales_data.dtypes) 
    print("\n" , sales_data.info)     # summary of dataframes
    print("\n" , sales_data.describe()) # basic stat of numerical colmuns  # include = 'all'

    print("\n" , sales_data.isnull().sum()) # missing values

    print("\n" ,sales_data['Quantity'].unique()) # unique categorical values
    print("\n" ,sales_data['Quantity'].value_counts())

    print("\n" , sales_data.duplicated()) # duplicate rows in df
except Exception as e:
    print("❌ Error loading CSV file:", e)
