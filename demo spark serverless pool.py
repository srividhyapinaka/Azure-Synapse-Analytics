#!/usr/bin/env python
# coding: utf-8

# ## demo spark serverless pool
# 
# 
# 

# In[2]:


df = spark.read.format('parquet')\
.load('abfss://srifilesystemsynpase@sriadlsgen2synpase.dfs.core.windows.net/userdata1.parquet')


# In[3]:


display(df.limit(10))


# In[4]:


df.printSchema()


# Load the user data into the spark user data Table

# In[5]:


spark.sql("CREATE DATABASE IF NOT EXISTS user_data")
df.write.mode("overwrite").saveAsTable("user_data")

