

# 2. Implement Multiple Linear Regression to predict the price.
# Fill null values with the median. Display the coefficients.

# Read data from the CSV file
df = pd.read_csv('HPriceData.csv') # Assuming HPriceData.csv is in the current directory. If not adjust the path

# Preprocessing
df = df.replace('?', np.nan)
df = df.apply(pd.to_numeric)
df = df.fillna(df.median())

# Regression
x = df.drop('Price', axis=1)
x.insert(0, 'x0', [1] * len(x))
x = x.values
x_transpose = x.T
x_transposeX = x_transpose.dot(x)
x_transposeX_inv = np.linalg.inv(x_transposeX)
y = df['Price'].values
x_transposeY = x_transpose.dot(y)
B_hat = x_transposeX_inv.dot(x_transposeY)
B0, B1, B2, B3 = B_hat[0], B_hat[1], B_hat[2], B_hat[3]
print("B0:", B0, "\nB1:", B1, "\nB2:", B2, "\nB3:", B3)

# Predictions
y_predicted_3 = B0 + (B1 * 3000) + (B2 * 3) + (B3 * 40)
print(f"Predicted Price for (3000, 3, 40): {y_predicted_3}")

y_predicted_4 = B0 + (B1 * 2500) + (B2 * 4) + (B3 * 5)
print(f"Predicted Price for (2500, 4, 5): {y_predicted_4}")




# prompt: give me above all code in one cell below 

import numpy as np
import pandas as pd

# 1 a. Implement Multilinear Regression on Data1.csv. Display the coefficients. (that is B1, B2, B3)
#   b. Predict Y values for 
#  Y  X1    X2    X3
#  ?  50    70    80
#  ?  30    40    50

# Read data from CSV file into a DataFrame
df = pd.read_csv('Data1.csv') # Assuming Data1.csv is in the current directory.  If not adjust the path.

# Create a new DataFrame 'x' by dropping the 'Y' column
x = df.drop('Y', axis=1)
x.insert(0, 'x0', [1] * len(x))
x = x.values
x_transpose = x.T
x_transposeX = x_transpose.dot(x)
x_transposeX_inv = np.linalg.inv(x_transposeX)
y = df['Y'].values
x_transposeY = x_transpose.dot(y)
B_hat = x_transposeX_inv.dot(x_transposeY)
B0, B1, B2, B3 = B_hat[0], B_hat[1], B_hat[2], B_hat[3]
print("B0:", B0, "\nB1:", B1, "\nB2:", B2, "\nB3:", B3)

# Predict Y for new data points
y_predicted_1 = B0 + (B1 * 50) + (B2 * 70) + (B3 * 80)
print(f"Predicted Y for (50, 70, 80): {y_predicted_1}")

y_predicted_2 = B0 + (B1 * 30) + (B2 * 40) + (B3 * 50)
print(f"Predicted Y for (30, 40, 50): {y_predicted_2}")
