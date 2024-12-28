import numpy as np
from sklearn.linear_model import Ridge

num_features = int(input("Enter number of features: "))
num_data_points = int(input("Enter number of data points: "))
print("Enter feature matrix row by row:")
X = np.array([list(map(float, input().split())) for _ in range(num_data_points)])
print("Enter target values:")
y = np.array(list(map(float, input().split())))

alpha = float(input("Enter regularization strength (alpha): "))
ridge_model = Ridge(alpha=alpha)
ridge_model.fit(X, y)

print(f"Coefficients: {ridge_model.coef_}")
print(f"Intercept: {ridge_model.intercept_}")