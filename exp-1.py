#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr = np.array([10,20,30,40,50])


# In[4]:


print("Numpy Array:")
print(arr)


# In[5]:


print("\n-- array indexing--\n")
print("First element:",arr[0])
print("Second element:",arr[1])
print("Third element:",arr[2])


# In[27]:


print("\n-- Array slicing--\n")
print("First three elements:",arr[0:3])
print("Elements from index 2:",arr[2:])
print("Last three elements:",arr[-3:])


# In[11]:


print("\n-- Basic Mathematical operations --\n")
print("Addition of array elements :",np.sum(arr))
print("Mean of array elements :",np.mean(arr))
print("Maximum of array elements :",np.max(arr))
print("Minimum of array elements :",np.min(arr))


# In[10]:


print("\n-- Basic Array operations --\n")
print("Add 5 :",arr+5)
print("Subtract 5 :",arr-5)
print("Multiply by 2 :",arr*2)
print("Divide by 10 :",arr/10)


# In[12]:


print("\n-- Array Reshaping--\n")
reshaped_arr = arr.reshape(5,1)
print("Reshaped array:\n",reshaped_arr)


# In[13]:


import pandas as pd 


# In[15]:


data = {
    "Name" : ["Asha", "Ravi","Meera","Karan"],
    "Marks":[88,72,91,65],
    "Branch":["CSE" , "ECE" , "CSE","ISE"]
}


# In[16]:


df = pd.DataFrame(data)
print("\n-- Pandas DataFrame --\n")
print(df)


# In[17]:


print("\n--Comuln Indexing--\n")
print("Name Column:\n",df["Name"])
print("Marks Column:\n",df["Marks"])


# In[18]:


print("\n--Row Indexing--\n")
print("First row :\n",df.iloc[0])
print("Third row:\n",df.iloc[2])


# In[21]:


print("\n--Specific Value--\n")
print("Marks of first student:",df.iloc[0,1])


# In[22]:


print("\n--Row slicing--\n")
print("First two rows:\n",df.iloc[0:2])


# In[23]:


print("\n--Row and Comuln slicing--\n")
print("First three rows with name and marks:\n",df.iloc[0:3,[0,1]])


# In[25]:


print("\n--Data filtering--\n")
result = df[df["Marks"]>70]
print("Students with marks greater than 70 :\n",result)


# In[ ]:




