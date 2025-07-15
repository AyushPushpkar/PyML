import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Generate synthetic dataset
# -------------------------------
np.random.seed(0)
n = 100

ages = np.random.randint(22, 60, size=n)
countries = np.random.choice(['India', 'USA', 'UK'], size=n)

# Simulate balance with trends based on country and age
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

# ---------------------------------------
# 📊 Pair Plot with KDE on diagonals
# ---------------------------------------
try:
    sns.set_theme(style="whitegrid")
    sns.pairplot(df, hue='Country', diag_kind='kde', palette='Set2')
    plt.suptitle("Pair Plot with KDE on Diagonals", y=1.02)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("Error during KDE pair plot:", e)

# ---------------------------------------
# 📊 Pair Plot with Histogram on diagonals
# ---------------------------------------
try:
    sns.set_theme(style="whitegrid")
    sns.pairplot(df, hue='Country', diag_kind='hist', palette='Set2')
    plt.suptitle("Pair Plot with Histogram on Diagonals", y=1.02)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("Error during histogram pair plot:", e)
