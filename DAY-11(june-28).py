#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Object Oriented Programming 
def test():
    print("test() for function")
    return
test()


# In[3]:


class demo:
    def test(self):
        print("test() for the class and method")
        return
obj=demo()
obj.test()


# In[9]:


class demo1:
    def fact(self,n):
        #return the factorial
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact
p1=demo1()
p1.fact(5)
       


# In[ ]:


#method
#def test(self,para1,para2)


# In[1]:


class demo2:
   
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        
    def add(self,p1,p2):
        return p1+p2
       
c1=demo2(10,20)
print(c1.add(100,200))


# In[11]:


#some inheritance
class person(object):
    #constructor
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isEmployee(self):
        return False
    
class Employee(person):
    def isEmployee(self):
        return True
emp=person("anil")
print(emp.getname(),emp.isEmployee())
emp1=Employee("akhil")
print(emp1.getname(),emp1.isEmployee())


# In[13]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
print(array.shape)
print(array.dtype)


# In[14]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
print(array)


# 

# In[15]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1.shape)
a2=np.array([(1,2),(3,4),(5,6)])
print(a2.shape)


# In[16]:


##re shape the given array
a1=np.array([(1,2,3),(4,5,6)])
print(a1)
a1.reshape(3,2)


# In[17]:


##append some data--horizotally
##append some data--vertically
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.hstack((a1,a2)))


# In[18]:


#vstack(array1,array2)--will be automatically arranged
##append some data--vertically
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.vstack((a1,a2)))


# In[37]:


##append some data--vertically
a1=np.array([1,2,3])
a2=np.array([4,5,6])
a3=np.array(list(map(int,(input().split(' ')))))
print(np.diagonal((a1,a2,a3)))


# In[19]:


#generate random numbers from np
a1=np.random.normal(5,0.5,10)
print(a1)


# In[20]:


#numpy.zeros() and numpy.one()
#generate an array with all zeros--numpy.zeros()
#numpy.zeros(shape,dtype=float,order="c")
np.zeros((2,2))


# In[21]:


np.zeros((2,2),dtype=np.int64)


# In[22]:


#np.ones(shape,dtype=float,order="c")
np.ones((4,3),dtype=np.int64)


# In[39]:


a=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(a)[2]=5
print(a)


# In[45]:


import numpy as np
np.arange(1,10)


# In[44]:


import numpy as np
np.arange(1,100,9)


# In[47]:


np.arange(2,20,2)
np.arange(1,25,2)


# In[49]:


a1=np.array([(1,2,3),(4,5,6)])
print("first row:",a1[0])


# In[51]:


a1=np.array([(1,2,3),(4,5,6)])
print("second row:",a1[1])


# In[52]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing column:",a1[:,1])


# In[53]:


a1=np.array([(1,2,3),(4,5,6)])

print("slicing last column:",a1[:,2])


# In[55]:


a1=np.random.normal(5,1,10)
print(a1)
print("min value=",np.min(a1))
print("max value=",np.max(a1))
print("mean value=",np.mean(a1))
print("median value=",np.median(a1))


# In[56]:


#multiply of 1d arrays
#numpy.dot(x,y)
c1=np.array([1,2])
c2=np.array([4,5])
np.dot(c1,c2)


# In[58]:


c1=np.array([(1,2),(3,4)])
c2=np.array([(3,4),(1,2)])
np.dot(c1,c2)


# In[59]:


b1=np.array([(1,2),(3,4)])
b2=np.array([(3,4),(1,2)])
np.matmul(b1,b2)


# In[60]:


np.zeros(3)


# In[2]:


import pandas as pd
dict1={"Name":["Anil","Akhil","Dinesh","Harsha","Ajay",'karanth'],"EmailID":["anil@gmail.com","akhil@gmail.com","dinesh@gmail.com","harsha@gmail.com","ajay@gmail.com","karanth@gmail.com"],
                        "Mobile Number":[999,888,777,888,777,999],"Address":["Hyd","Hyd","Hyd","Hyd","Hyd","Hyd"]}
b=pd.DataFrame(dict1)
print(b)
                                                                               
                                                                           


# In[ ]:




