#!/usr/bin/env python
# coding: utf-8

# # Telco_Churn_Data_Analysis 

# In[26]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[27]:


df= pd.read_csv("E:/CODING/project/DataSetVisualizeton/Customer Churn.csv")
df


# In[28]:


df.info()


# In[29]:


df["TotalCharges"]=df["TotalCharges"].replace(" ","0")
df["TotalCharges"]=df["TotalCharges"].astype("float")


# In[30]:


df.isnull().sum()


# In[31]:


df.describe()


# In[32]:


df["customerID"].duplicated().sum()


# In[33]:





# In[38]:


ax=sns.countplot(x="Churn", data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of Churn")
plt.show()


# In[39]:


gb= df.groupby("Churn").agg({"Churn":"count"})
plt.pie(gb["Churn"], labels=gb.index, autopct="%1.2f%%")
plt.title("percentage of Churned customer")
plt.show


# In[44]:


ax=sns.countplot(x="gender", data=df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn by Gender")


# In[45]:


ax=sns.countplot(x="SeniorCitizen", data=df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn by SeniorCitizen")


# In[47]:


counts = df.groupby(['SeniorCitizen', 'Churn']).size().unstack()
percentages = counts.div(counts.sum(axis=1), axis=0) * 100  # Calculate percentages

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Create the bars for each category in a stacked manner
bottom_val = [0] * len(percentages)  # Initialize bottom values for stacking
for churn_status in percentages.columns:
    # Plot each bar segment
    ax.bar(percentages.index, percentages[churn_status], bottom=bottom_val, label=f'Churn: {churn_status}')

    # Add text labels for each bar segment
    for i, pct in enumerate(percentages[churn_status]):
        ax.text(i, bottom_val[i] + pct / 2, f"{pct:.1f}%", ha="center", va="center", color="white", fontsize=10)
    
    # Update the bottom values for the next segment
    bottom_val += percentages[churn_status]

# Add labels and title
ax.set_title("Churn by SeniorCitizen (Percentage)")
ax.set_xlabel("Senior Citizen")
ax.set_ylabel("Percentage")
ax.legend(title="Churn")
plt.show()


# In[50]:


sns.histplot(x="tenure", data=df, bins=50, hue="Churn")
plt.title("Churn by tenure")


# In[53]:


ax=sns.countplot(x="Contract", data=df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churn of Customer by Contract")


# In[54]:


df.columns.values


# In[58]:


columns_to_plot = [
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Set up the number of rows and columns for the subplots
n_cols = 3  # Number of columns in the subplot grid
n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols  # Calculate number of rows needed

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
axes = axes.flatten()  # Flatten the array of axes for easy iteration

# Loop through each column and create a count plot
for i, column in enumerate(columns_to_plot):
    sns.countplot(x=column, data=df, ax=axes[i], palette="Set2", hue=df["Churn"])
    axes[i].set_title(f'Count of {column}')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Count')

# Hide any unused subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()  # Adjust layout for better spacing
plt.show()


# In[ ]:




