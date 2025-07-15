import pandas as pd

# Sample data for January
january_data = {
    "Product": ["Shirt", "Pants", "Shoes"],
    "Sales": [100, 150, 200]
}

# Sample data for March
march_data = {
    "Product": ["Jacket", "Hat", "Socks"],
    "Sales": [300, 120, 180]
}

# Convert to DataFrames
df_january = pd.DataFrame(january_data)
df_march = pd.DataFrame(march_data)

# Save to Excel with multiple sheets
try:
    with pd.ExcelWriter("C:/Users/ayush/Jupyter/sales_data.xlsx", engine='openpyxl') as writer:
        df_january.to_excel(writer, sheet_name="January", index=False)
        df_march.to_excel(writer, sheet_name="March", index=False)
    print("✅ Excel file with multiple sheets created successfully!")
except Exception as e:
    print("❌ Failed to create Excel file:", e)
