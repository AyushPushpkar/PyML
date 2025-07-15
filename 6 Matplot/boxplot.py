import numpy as np
import matplotlib.pyplot as plt

try:
    # Set random seed for reproducibility
    np.random.seed(0)

    # Generate random data for 3 product categories
    data = [
        np.random.normal(loc=50, scale=20, size=100),  # Shirts
        np.append(np.random.normal(60, 7, size=95), [100, 105, 110]),  # Pants with outliers
        np.random.normal(55, 10, size=100)  # Shoes
    ]

    # Product labels
    labels = ['Shirts', 'Pants', 'Shoes']

    # Create the box plot
    plt.figure(figsize=(6, 4))
    plt.boxplot(
        data,
        tick_labels=labels,
        patch_artist=True,  # Fill the boxes with color
        boxprops=dict(facecolor='skyblue'),  # Box fill color
        flierprops=dict(marker='o', markerfacecolor='red')  # Style for outliers
    )

    # Add labels and title
    plt.title("Product Sales Distribution (Box Plot)")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Show the plot
    plt.show()

except Exception as e:
    print("Error:", e)
