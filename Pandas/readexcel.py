import pandas as pd

try:
    # Read the Excel file (sheet_name can be omitted if you want the first sheet)
    excel_data = pd.read_excel("C:/Users/ayush/Jupyter/sales_data.xlsx" , sheet_name=["January", "March"])
    print("✅ Excel file loaded successfully!")
    print(excel_data["January"].head())
except Exception as e:
    print("❌ Error loading Excel file:", e)
