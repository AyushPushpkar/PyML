import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    # sns.set(style = "whitegrid")  
    sns.set_theme(style="whitegrid")


    # Set random seed for reproducibility
    np.random.seed(0)

    # Generate synthetic data
    df = pd.DataFrame({
        'Age': np.random.randint(20, 60, 100),
        'Balance': np.random.normal(loc=1500, scale=500, size=100)
    })

    # Create subplots
    plt.figure(figsize=(10, 4))

    # Histogram + KDE for Age
    plt.subplot(1, 2, 1)
    sns.histplot(df["Age"], kde=True, color='cornflowerblue', bins=5 ) #In Seaborn, kde=True enables a Kernel Density Estimate (KDE) 
    # line over your histogram. It gives a smoothed curve representing the probability density function (PDF) of the continuous variable.
    plt.title("Age Distribution with KDE")
    plt.xlabel("Age")
    plt.ylabel("Density")

    # Histogram + KDE for Balance
    plt.subplot(1, 2, 2)
    sns.histplot(df["Balance"], kde=True, color='seagreen', bins=5)
    plt.title("Balance Distribution with KDE")
    plt.xlabel("Balance")
    plt.ylabel("Density")

    # Adjust layout and show
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
