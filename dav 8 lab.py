#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Input data: Study Hours
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Output data: Marks
y = np.array([40, 50, 55, 70, 75])

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Display slope and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])

# Draw actual data points
plt.scatter(X, y, color="blue", label="Actual Marks")

# Draw regression line
plt.plot(X, model.predict(X),
         color="red", label="Regression Line")


# In[2]:


# Display predicted point
plt.scatter(6, prediction[0],
            color="green", s=100, marker="*",
            label="Predicted Marks")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Student Marks")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




