#!/usr/bin/env python
# coding: utf-8

# ## continue to demo spark serverless pool
# 
# 
# 

# In[6]:


df1 = spark.sql("select * from user_data")


# In[8]:


display(df1)


# In[13]:


spark.sql("SELECT first_name, last_name FROM user_data WHERE gender = 'Female'")

