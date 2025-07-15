import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # Seed for reproducibility
    np.random.seed(0)

    n = 100

    # Generate ages and countries
    ages = np.random.randint(22, 60, size=n)
    countries = np.random.choice(['India', 'USA', 'UK'], size=n)

    # Generate balances based on age and country
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

    # Create DataFrame
    df = pd.DataFrame({
        'Age': ages,
        'Balance': balances,
        'Country': countries
    })

    # Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Age', y='Balance', hue='Country', palette='Set2', size='Balance', sizes=(40, 200))

    plt.title("Scatter Plot of Balance vs Age (colored by Country)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("An error occurred:", e)
