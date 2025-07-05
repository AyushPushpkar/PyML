import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# 📊 Bar Plot in try block
# ----------------------------
try:
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='Country', y='Balance', estimator=np.mean, ci='sd', palette='pastel')
    
    plt.title("Average Balance by Country")
    plt.xlabel("Country")
    plt.ylabel("Average Balance")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("Error while plotting bar plot:", e)
