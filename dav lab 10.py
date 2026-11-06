#!/usr/bin/env python
# coding: utf-8

# In[1]:


# MULTIPLE LINEAR REGRESSION

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 2. Create dataset
data = {
    'StudyHours': [1, 2, 3, 4, 5],
    'Attendance': [40, 20, 60, 100, 80],
    'Marks': [18, 17, 25, 33, 32]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# 3. Define independent and dependent variables
X = df[['StudyHours', 'Attendance']]
y = df['Marks']

# 4. Create Multiple Linear Regression model
model = LinearRegression()

# 5. Train the model
model.fit(X, y)

# 6. Predict marks
y_pred = model.predict(X)

print("\nActual Marks:", list(y))
print("Predicted Marks:", y_pred)

# 7. Display model coefficients
print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# 8. Evaluate the model
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

print("\nR2 Score:", r2)
print("Mean Squared Error:", mse)

# 9. Predict marks for a new student
new_student = pd.DataFrame({
    'StudyHours': [6],
    'Attendance': [90]
})

predicted_marks = model.predict(new_student)

print("\nPredicted Marks for New Student:",
      predicted_marks[0])

# 10. Visualize actual vs predicted marks
plt.scatter(y, y_pred, color='blue', label='Predicted Marks')
plt.plot([min(y), max(y)], [min(y), max(y)],
         color='red', label='Perfect Prediction')

plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Multiple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()


# In[2]:


# 5. Train the model
model.fit(X, y)

# 6. Display intercept and coefficients
print("\nIntercept:", model.intercept_)
print("Study Hours Coefficient:", model.coef_[0])
print("Attendance Coefficient:", model.coef_[1])

# 7. Display regression equation
print("\nRegression Equation:")

print(
    f"Marks = {model.intercept_:.2f} "
    f"+ {model.coef_[0]:.2f} * StudyHours "
    f"+ {model.coef_[1]:.2f} * Attendance"
)

# 8. Predict marks for all students
y_pred = model.predict(X)

df['PredictedMarks'] = y_pred

print("\nActual vs Predicted Marks:")
print(df)


# In[3]:


# 9. Predict marks for a new student

new_student = pd.DataFrame({
    'StudyHours': [6],
    'Attendance': [90]
})

new_prediction = model.predict(new_student)

print("\nNew Student Details:")
print(new_student)

print("Predicted Marks:", new_prediction[0])


# 10. Calculate R-squared

r2 = r2_score(y, y_pred)

print("\nR-squared:", r2)
print("R-squared Percentage:", r2 * 100, "%")


# 11. Calculate RMSE

mse = mean_squared_error(y, y_pred)

rmse = np.sqrt(mse)

print("\nMean Squared Error:", mse)
print("RMSE:", rmse)


# In[4]:


# 12. Visualization 1: Actual vs Predicted Marks

plt.figure(figsize=(7, 5))

plt.scatter(y, y_pred, s=100, label="Predicted Marks")

plt.plot(
    [y.min(), y.max()],
    [y.min(), y.max()],
    linestyle='--',
    label="Perfect Prediction"
)

plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted Marks")

plt.legend()
plt.grid()
plt.show()


# In[5]:


# 13. Visualization 2: Residual Plot

residuals = y - y_pred

plt.figure(figsize=(7, 5))

plt.scatter(y_pred, residuals, s=100)

plt.axhline(y=0, linestyle='--')

plt.xlabel("Predicted Marks")
plt.ylabel("Residuals (Actual - Predicted)")
plt.title("Residual Plot")

plt.grid()
plt.show()


# In[9]:


# 14. Visualization 3: Regression Plane

fig = plt.figure(figsize=(9, 6))

ax = fig.add_subplot(111, projection='3d')

study_range = np.linspace(1, 5, 20)
attendance_range = np.linspace(20, 100, 20)

study_grid, attendance_grid = np.meshgrid(
    study_range, attendance_range
)

plane_input = pd.DataFrame({
    'StudyHours': study_grid.ravel(),
    'Attendance': attendance_grid.ravel()
})

marks_grid = model.predict(plane_input).reshape(study_grid.shape)

ax.plot_surface(
    study_grid,
    attendance_grid,
    marks_grid,
    alpha=0.5
)

ax.scatter(
    df['StudyHours'],
    df['Attendance'],
    df['Marks'],
    s=80,
    label="Actual Students"
)
ax.set_xlabel("Study Hours")
ax.set_ylabel("Attendance Percentage")
ax.set_zlabel("Marks")

ax.set_title("Multiple Linear Regression Plane")
ax.legend()

plt.show()


# In[8]:





# In[ ]:




