#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Import the libraries
import pandas as pd
print(1)
import plotly.express as px
import plotly.graph_objects as go


# In[29]:


#load data
data = pd.read_csv('C:\\Users\\chauhan.payal\\Downloads\\Basic_LinkedInDataExport_02-27-2021\\Connections.csv')
data.head(20)


# In[30]:


# Describe the data
data.describe()


# In[31]:


# Convert the 'Connected On' column to datetime format
data["Connected On"] = pd.to_datetime(data["Connected On"])
data["Connected On"]


# In[32]:


# Create a line plot to visualize the number of connections on a given date
fig1 = px.line(data.groupby(by="Connected On").count().reset_index(), 
               x="Connected On", 
               y="First Name", 
               labels={"First Name": "Count"},
               title="Number of Connections on a Given Date")
fig1.show()


# In[33]:


# Group and sort the data by company 
df_by_company = df.groupby(by="Company").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
df_by_company


# In[34]:


# Create a bar plot for the top companies
fig2 = px.bar(df_by_company[:20],
              x="Company",
              y="First Name",
              labels={"First Name": "Count"},
              title="Top Companies/Organizations in my Network")
fig2.show()


# In[35]:


# Create a treemap for the top companies
fig3 = px.treemap(df_by_company[:100], path=["Company", "Position"],
                 values="First Name",
                 labels={"First Name": "Count"})
fig3.show()


# In[36]:


# Group and sort the data by position 
df_by_position = df.groupby(by="Position").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
df_by_position


# In[37]:


# Create a bar plot for the top positions
fig4 = px.bar(df_by_position[:20],
              x="Position",
              y="First Name",
              labels={"First Name": "Count"},
              title="Top Positions in my Network")
fig4.show()


# In[38]:


# Create a treemap for the top positions
fig5 = px.treemap(df_by_position[:100], path=["Position", "Company"],
                 values="First Name",
                 labels={"First Name": "Count"})
fig5.show()


# In[40]:


# Find all positions that contains 'Data Engineer'
df["Position"].str.contains("Data Engineer").sum()


# In[ ]:




