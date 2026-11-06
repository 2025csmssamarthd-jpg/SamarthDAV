#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Input data: Study Hours
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Actual output: Marks
y = np.array([40, 50, 55, 70, 75])

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict marks for the original students
y_pred = model.predict(X)

# Calculate R-squared
r2 = r2_score(y, y_pred)

# Calculate RMSE
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

# Display evaluation results
print("R-squared:", r2)
print("R-squared Percentage:", r2 * 100, "%")
print("RMSE:", rmse)


# In[2]:


# Predict marks for a new student
prediction = model.predict([[6]])
print("Predicted Marks for 6 Hours:", prediction[0])

# Plot actual data and regression line
plt.scatter(X, y, color="blue", label="Actual Marks")
plt.plot(X, y_pred, color="red", label="Regression Line")

# Show the new predicted point
plt.scatter(6, prediction[0], color="green",
            marker="*", s=150, label="New Prediction")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




