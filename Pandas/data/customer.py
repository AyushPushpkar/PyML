import pandas as pd

# Sample customer data
customer_data = {
    "CustomerID": ["C001", "C002", "C003", "C004", "C005"],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Country": ["India", "USA", "UK", "India", "Germany"],
    "Age": [28, 34, 45, 25, 31],
    "Balance": [1500.75, 820.00, 2340.50, 1190.25, 560.00]
}

# Convert to DataFrame
customers_df = pd.DataFrame(customer_data)

# Save to CSV
try:
    customers_df.to_csv("C:/Users/ayush/Jupyter/customers.csv", index=False)
    print("✅ Customer CSV saved successfully!")
except Exception as e:
    print("❌ Failed to save customer CSV:", e)
