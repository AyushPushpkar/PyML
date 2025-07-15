from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

X = pd.DataFrame({
    'feature1': [10, 20, 30, 40, 50, 60, 70, 80],
    'feature2': [5, 15, 25, 35, 45, 55, 65, 75]
})
y = pd.Series([100, 150, 200, 250, 300, 350, 400, 450], name='target')


# Step 1: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2a: StandardScaler (Z-score normalization)
standard_scaler = StandardScaler()
X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)

# Step 2b: MinMaxScaler (scaling to [0, 1])
minmax_scaler = MinMaxScaler()
X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

# Optional: convert back to DataFrame if needed
X_train_standard = pd.DataFrame(X_train_standard, columns=X.columns)
X_test_standard = pd.DataFrame(X_test_standard, columns=X.columns)

X_train_minmax = pd.DataFrame(X_train_minmax, columns=X.columns)
X_test_minmax = pd.DataFrame(X_test_minmax, columns=X.columns)

# Done: You now have both versions ready for modeling
print("Standard Scaled Train Set:\n", X_train_standard.head())
print("MinMax Scaled Train Set:\n", X_train_minmax.head())


# standard scaler : Works well with algorithms that assume data is normally distributed:
# e.g., Linear Regression, Logistic Regression, SVM, K-Means, PCA

# minmax scaler : Useful for Neural Networks, KNN, and gradient-based algorithms like SGD.