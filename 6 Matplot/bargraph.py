import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

try:
    # Set random seed for reproducibility
    np.random.seed(0)

    # Define product categories
    categories = ['Shirt', 'Pants', 'Shoes', 'Hat', 'Socks']

    # Generate random sales data (e.g., total sales per product)
    sales = np.random.randint(100, 1000, size=len(categories))

    # Generate gradient colors from the 'plasma' colormap (left to right)
    colors = [cm.plasma(i) for i in np.linspace(0, 1, len(categories))]

    # Create the bar plot
    plt.figure(figsize=(6, 4))
    plt.bar(categories, sales, color=colors)

    # Add plot labels and title
    plt.title("Product Sales Bar Plot")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Show the plot
    plt.show()

except Exception as e:
    print("Error:", e)
