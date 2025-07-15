import pandas as pd
import matplotlib.pyplot as plt

try:
    transaction_df = pd.read_csv("C:/Users/ayush/Jupyter/transaction_data.csv") 
    customer_df = pd.read_csv("C:/Users/ayush/Jupyter/customers.csv")

    transaction_df['Date'] = pd.to_datetime(transaction_df['Date'])

    merged_df = pd.merge(transaction_df , customer_df , on = 'CustomerID' , how = 'inner')

    country_summary = merged_df.groupby('Country').agg({'Quantity' : 'sum' , 'Total' : 'sum'})

    country_summary = merged_df.groupby('Country').agg({
        'Quantity': ['sum', 'mean', 'max', 'min'],
        'Total': ['sum', 'mean', 'std'],
        'CustomerID': 'nunique'
    })

    country_summary.plot(
        kind='pie',
        y='Total',
        autopct='%1.1f%%',
        figsize=(8, 8),
        legend=False,
        title='Sales Distribution by Country',
        subplots=True
    )

    plt.ylabel('')
    plt.tight_layout()
    plt.show()



    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 'Total' → 'sum'
    country_summary[('Total', 'sum')].plot.pie(
        ax=axs[0],
        autopct='%1.1f%%',
        title='Total Sales (Sum)'
    )

    # Plot 'Total' → 'mean'
    country_summary[('Total', 'mean')].plot.pie(
        ax=axs[1],
        autopct='%1.1f%%',
        title='Total Sales (Mean)'
    )

    plt.tight_layout()
    plt.show()
except Exception as e:
    print("❌ Error :", e)