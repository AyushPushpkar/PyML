import pandas as pd

# Create some sample data
data = {
    "Product": ["Shirt", "Pants", "Shoes", "Shoes", "Hat", "Tie", "Shirt", "Shoes"],
    "Price": [500, 800, 1500, 1500, 300, None, 500, 1500],
    "Quantity": [10, 20, 15, 15, 5, 12, None, 15],
    "Category": ["Clothing", "Clothing", "Footwear", "Footwear", "Accessories", "Accessories", "Clothing", "Footwear"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV with a correct path
try:
    df.to_csv("C:/Users/ayush/Jupyter/sales_data.csv", index=False)
    print("✅ CSV file saved successfully!")
except Exception as e:
    print("❌ Failed to save CSV:", e)


