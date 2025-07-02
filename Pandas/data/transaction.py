import pandas as pd

# Simulated transaction data
data = {
    "TransactionID": [1001, 1002, 1003, 1004, 1004, 1005, 1006, 1007],
    "Date": ["2025-07-01", "2025-07-01", "2025-07-02", "2025-07-03", "2025-07-03", "2025-07-04", "2025-07-05", "2025-07-05"],
    "CustomerID": ["C001", "C002", "C003", "C004", "C004", "C005", "C001", "C001"],
    "Product": ["Shirt", "Pants", "Shoes", "Shoes", "Shoes", "Hat", "Pants", "Shirt"],
    "Quantity": [1, 2, 1, 1, 1, 2, 1, 3],
    "Price": [500, 800, 1500, 1500, 1500, 300, 800, 500],
    "PaymentMethod": ["Card", "Cash", "UPI", "Card", "Card", "UPI", "Cash", "Card"]
}

# Compute total (Quantity * Price), handling None values
df = pd.DataFrame(data)
df["Total"] = df["Quantity"] * df["Price"]

# Save to CSV
try:
    df.to_csv("C:/Users/ayush/Jupyter/transaction_data.csv", index=False)
    print("✅ Transaction CSV saved successfully!")
except Exception as e:
    print("❌ Failed to save CSV:", e)
