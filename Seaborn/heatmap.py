import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# Data Preparation (Same as before)
# ----------------------------
np.random.seed(0)
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

# ----------------------------
# 🔥 Heatmap of Correlation
# ----------------------------
try:
    # Compute correlation matrix (only numeric columns)
    corr = df[['Age', 'Balance']].corr()

    # Plot heatmap
    plt.figure(figsize=(5, 4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", square=True, cbar=True)

    plt.title("Correlation Heatmap: Age vs Balance")
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error while plotting heatmap:", e)
