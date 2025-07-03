import pandas as pd
import matplotlib.pyplot as plt

try:
    transaction_df = pd.read_csv("C:/Users/ayush/Jupyter/transaction_data.csv") 
    customer_df = pd.read_csv("C:/Users/ayush/Jupyter/customers.csv")

    transaction_df.head()
    customer_df.head()
    transaction_df.info()
    customer_df.info()

    transaction_df['Date'] = pd.to_datetime(transaction_df['Date'])
    customer_df['CustomerID'].value_counts().sum()

    transaction_df['CustomerID'].nunique() # how many purchased

    merged_df = pd.merge(transaction_df , customer_df , on = 'CustomerID' , how = 'inner')

    age_summary = merged_df.groupby('Age')['Quantity'].sum() # groupby age and sum the related quantity
    country_summary = merged_df.groupby('Country').agg({'Quantity' : 'sum' , 'Total' : 'sum'})

    country_summary = merged_df.groupby('Country').agg({
        'Quantity': ['sum', 'mean', 'max', 'min'],
        'Total': ['sum', 'mean', 'std'],
        'CustomerID': 'nunique'
    })

    country_summary['Total'].plot(kind= 'bar' ,figsize = (8,4) , title = 'Total sales by country')


except Exception as e:
    print("❌ Error :", e)