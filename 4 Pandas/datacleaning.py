import pandas as pd

try:
    df = pd.read_csv("C:/Users/ayush/Jupyter/sales_data.csv")
    print("✅ CSV file loaded successfully!")
    print(df.head()) # top 5 records
    print("\n" , df.tail())

    print("\n" , df.isnull().sum()) # missing values

    # fill missing values with the median
    df['Price'] = df['Price'].fillna(df['Price'].median())
    df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

    print(df.duplicated().sum()) #duplicates
    df.drop_duplicates(inplace=True) #  remove duplicates

     
    #corecting data type of coloumn
    df['Quantity'] = df['Quantity'].astype(int)

    #ensure price is positive
    df['Price'] = df[df['Price'] >= 0 ]

except Exception as e:
    print("❌ Error loading CSV file:", e)