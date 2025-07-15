import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # Set random seed for reproducibility
    np.random.seed(0)

    # Generate a 5x5 matrix of random integers between 10 and 100
    data = np.random.randint(10, 100, size=(5, 5))

    # Labels for rows and columns (optional)
    row_labels = ['A', 'B', 'C', 'D', 'E']
    col_labels = ['P1', 'P2', 'P3', 'P4', 'P5']

    # Create the heatmap using seaborn
    plt.figure(figsize=(6, 4))
    sns.heatmap(data, annot=True, fmt="d", cmap='YlGnBu',
                xticklabels=col_labels, yticklabels=row_labels,
                cbar=True, linewidths=0.5, linecolor='gray')

    # Add title
    plt.title("Sales Heatmap")
    plt.tight_layout()

    # Display the heatmap
    plt.show()

except Exception as e:
    print("Error:", e)
