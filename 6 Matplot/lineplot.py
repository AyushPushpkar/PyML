import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try :
    transaction_df = pd.read_csv("C:/Users/ayush/Jupyter/transaction_data.csv")
    transaction_df['Date'] = pd.to_datetime(transaction_df['Date'])
    transaction_df['Price'] = transaction_df['Price'].astype(float)
    transaction_df['Total'] = transaction_df['Total'].astype(float)
    transaction_df.drop_duplicates(inplace= True)

    # Group and sum total sales by product
    product_sales = transaction_df.groupby("Product")["Total"].sum()
    
    plt.figure(figsize=(6, 4))  

    # Plot the data: X = product names, Y = total sales
    plt.plot(
        product_sales.index,       # X-axis: product names (Shirt, Pants, etc.)
        product_sales.values,      # Y-axis: total sales for each product
        marker='o',                # 'o' places a circular marker on each data point
        linestyle='-',             # '-' draws solid lines between points
        color='b'                  # 'b' sets the line color to blue
    )

    plt.title("Product Sales Data")    # You can also add parameters like fontsize=14, color='red', etc.
    plt.xlabel("Product")  
    plt.ylabel("Total Sales") 

    plt.grid(True)  # Can also use: plt.grid(axis='y', linestyle='--', color='gray')

    # Automatically adjust layout to prevent label/graph cutoff
    plt.tight_layout()  # Helps avoid overlapping labels/titles on smaller figures

    # Display the plot
    plt.show()  # Final rendering of the plot on screen   
except Exception as e :
    print("Error : " , e)
