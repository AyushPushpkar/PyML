import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    # Set random seed for reproducibility
    np.random.seed(0) # It ensures that you get the same sequence of random numbers every time you run the code.

    # Generate random data (e.g., 1000 values from a normal distribution)
    data = np.random.normal(loc=0, scale=1, size=1000)
    # data = np.random.randn(1000)  # Mean = 0, Std Dev = 1
 
    # Create histogram
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30, color='skyblue', edgecolor='black')  # 30 bins for better resolution

    # Titles and labels
    plt.title("Histogram of Randomly Generated Data (Normal Distribution)")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()
except Exception as e :
    print("Error : " , e)    