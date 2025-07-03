import matplotlib.pyplot as plt
import pandas as pd

try:
    # Sample Data (replace with your own DataFrame if needed)
    data = {
        "Product": ["Shirt", "Pants", "Shoes", "Hat", "Shirt", "Pants"],
        "Total": [500, 1600, 1500, 600, 1500, 800]
    }
    
    df = pd.DataFrame(data)

    # Optional: Convert Total to float
    df["Total"] = df["Total"].astype(float)

    # Generate random data
    # x = np.random.rand(50) * 10   # 50 random x values between 0 and 10
    # y = np.random.rand(50) * 100  # 50 random y values between 0 and 100

    # Create scatter plot
    plt.figure(figsize=(6, 4))
    plt.scatter(df["Product"], df["Total"], color='green', marker='o')

    # Plot decorations
    plt.title("Scatter Plot of Product vs Total Sales")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error while plotting scatter plot:", e)
