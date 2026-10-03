#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd 
df = pd.DataFrame({
   "order data  " : [
       "2024-01-10",
       "2024-01-15",
       "2024-02-05",
       "2024-02-12",
       "2024-03-01",
       "2024-03-15",
       "2024-04-10",
       "2024-04-20",
       "2024-05-05",
       "2024-01-15"
   ],
    "Product name" :[
        "Laptop",
        "Mouse",
        "Printer",
          "Tablet",
          "Laptop",
          "Monitor",
          "Mouse",
          "Printer",
          "Smartwatch",
          "mouse"
    ],
    
"Category":[
    "Electronics",
    "Accessories",
    "office",
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "office",
    "Electronics",
    "Accessories"
    
],
    "Region":[
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
        "East",
        "West",
        "North",
        "South"
    ],
    
"Quantity" :[
    2,
    5,
    3,
    4,
    1,
    2,
    6,
    2,
    3,
    5
],
    "Sales":[
        50000,
        2500,
        9000,
        30000,
        55000,
        16000,
        3000,
        6000,
        45000,
        2500
        
    ],
    
    "profit":[
        10000,
        500,
        1500,
        6000,
        11000,
        3000,
        None,
        1000,
        9000,
        500
    ],
})


# In[12]:


print("1. ORIGINAL DATASET")
print("-" *50)
display(df)


# In[13]:


print("2. FIRST 5 RECORDS")
print("-" *50)
display(df.head())


# In[18]:


print("4. DATASET SHAPE")
print("-" *50)
display(df.shape)


# In[19]:


print("5. COLUMN NAMES")
print("-" *50)
display(df.columns)


# In[17]:


print("3. LAST 5 RECORDS")
print("-" *50)
display(df.tail())


# In[21]:


print("6. DATA TYPES")
print("-" *50)
display(df.dtypes)


# In[23]:


print("7. DESCRIPTIVE STATISTICS")
print("-" *50)
display(df.describe())


# In[24]:


print("8.MISSING VALUES")
print("-" *50)
display(df.isnull().sum())


# In[26]:


print("9. ROWS CONTAINING MISSING VALUES")
print("-" *50)
display(df[df.isnull().any(axis=1)])


# In[27]:


print("10. TOTAL DUPLICTAES RECORDS")
print("-" *50)
display(df.duplicated().sum())


# In[29]:


print("11.  DUPLICTAES RECORDS")
print("-" *50)
display(df[df.duplicated()])


# In[46]:


new_sales = pd.DataFrame({
     "order data  " : [
       "2024-06-01",
       "2024-06-05",
       "2024-06-10"
   ],
    "Product name" :[
        "Laptop",
        "Mouse",
        "Printer"
         
    ],
    
"Category":[
    "Electronics",
    "Accessories",
    "office"
],
    "Region":[
        "North",
        "South",
        "East"
    ],
    
"Quantity" :[
    2,
    5,
    3
],
    "Sales":[
        60000,
        2000,
        9000
        
    ],
    
    "profit":[
        12000,
        400,
        1800
    ],
})


# In[31]:


print("11. NEW SALES DATASET")
print("-" *50)
display(new_sales)


# In[32]:


combined_df = pd.concat(
    [df,new_sales],
    ignore_index = True
)


# In[34]:


print("12. CONCANTENATED DATASET")
print("-" *50)
display(combined_df)


# In[47]:


product_info = pd.DataFrame({
    "Product name" :[
        "Laptop",
        "Mouse",
        "Printer",
          "Tablet",
          "Monitor"
         
    ],
    "Supplier":[
        "Dell",
        "Logitech",
         "HP",
        "Samsung",
         "LG"
    ],
    "Discount":[
        10,
        5,
        15,
        8,
        12
    ],
    
})


# In[36]:


print("13. PRODUCT INFOMATION DATASET")
print("-" *50)
display(product_info)


# In[48]:


merge_df=pd.merge(
df,
product_info,
on = "Product name",
how = "left"
)


# In[49]:


print("14. MERGED DATASET")
print("-" *50)
display(merge_df)


# In[53]:


region_info = pd.DataFrame({
    " Region_Manager" :[
        "Manager A",
        "Manager B",
        "Manager C",
        "Manager D"
    ]
         
        },
   
    index = [
        "North",
        "South",
        "East",
        "West"
    ]
        )


# In[55]:


print("14. REGION INFOMATION DATASET")
print("-" *50)
display(region_info)
df_region=df.set_index("Region")
joined_df=df_region.join(region_info)
print("15. JOINED INFOMATION DATASET")
print("-" *50)
display(joined_df)


# In[56]:


region_sales=df.groupby(
"Region"
)["Sales"].sum()


# In[57]:


print("16. TOTAL SALES BY REGION")
print("-" *50)
display(region_sales)


# In[59]:


pivot_table=pd.pivot_table(
df,
    values="Sales",
    index="Category",
    columns="Region",
    aggfunc="sum",
    fill_value = 0
)


# In[60]:


print("17. PIVOT TABLE")
print("-" *50)
display(pivot_table)


# In[ ]:




