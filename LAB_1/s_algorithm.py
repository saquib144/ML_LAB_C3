#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("data.csv")
print(data)


# In[3]:


d=np.array(data)[:,:-1]
print("The attributes are : \n",d)
target=np.array(data)[:,-1]
print("\nThe target is : ",target)


# In[4]:


def train(c,t):
  for i,val in enumerate(t):
    if val == "yes":
      specific_hypothesis=c[i].copy()
      break
  
  for i,val in enumerate(c):
    if t[i] == "yes":
      for x in range(len(specific_hypothesis)):
        if val[x] != specific_hypothesis[x]:
          specific_hypothesis[x] = '?'
        else:
          pass

  return specific_hypothesis


# In[5]:


print("The final hypothesis is : ",train(d,target))


# In[ ]:




