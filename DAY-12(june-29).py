#!/usr/bin/env python
# coding: utf-8

# In[2]:


#create a series by passing a list of values
import pandas as pd
a=pd.Series([1,3,4,5,6,7])
print(a)


# In[3]:


#missing values the it can be nan of numpy
import numpy as np
a1=pd.Series([1,2,3,4,np.nan,6])
print(a1)


# In[4]:


#create a list of data with in particular range
dates=pd.date_range('20190601',periods=20)
print(dates)


# In[ ]:


#creating a dict converted into series of values
a3=pd.DataFrame({'A':1.,
                'B':pd.Timestamp('20190601'),
                'C':pd.Series(1,index=list(range(4)),dtype='float32')
                'D':np.array([3]*4,dtype)})


# In[1]:


#drawing a square
import turtle as tt
a1=tt.Turtle()
a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

tt.done()


# In[ ]:


#drawing a star
import turtle as tt
a1

