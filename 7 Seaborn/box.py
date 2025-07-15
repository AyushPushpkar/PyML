import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # Sample data
    n = 100
    ages = np.random.randint(22, 60, size=n)
    countries = np.random.choice(['India', 'USA', 'UK'], size=n)
    balances = []

    for i in range(n):
        age = ages[i]
        country = countries[i]
        if country == 'India':
            balance = np.random.normal(loc=1000 + age * 5, scale=100)
        elif country == 'USA':
            balance = np.random.normal(loc=1500 + age * 7, scale=120)
        else:  # UK
            balance = np.random.normal(loc=1300 + age * 6, scale=110)
        balances.append(balance)

    df = pd.DataFrame({
        'Age': ages,
        'Balance': balances,
        'Country': countries
    })

    # Box plot with colored outliers
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x='Country',
        y='Balance',
        palette='pastel',
        flierprops=dict(marker='o', markerfacecolor='red', markersize=7, linestyle='none')  # outliers
    )

    plt.title("Box Plot of Balance by Country (with Red Outliers)")
    plt.xlabel("Country")
    plt.ylabel("Balance")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
