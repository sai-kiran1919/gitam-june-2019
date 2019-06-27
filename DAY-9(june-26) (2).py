#!/usr/bin/env python
# coding: utf-8

# In[2]:


##string functions-Built in functions
##upper()-returns strings which all the characters in upper case
str="lakalaka"
print(str.upper())
print(str.lower())


# In[5]:


##whether the given character is upper or not
##if it is upper it returns true otherwise it returns false
s="python is easy programming to learn"
s1='python'
s2="ABCd"
print(s.islower())
print(s1.islower())
print(s2.isupper())


# In[6]:


s="52345"
s1="ewqr445"
print(s.isnumeric())
print(s1.isnumeric())


# In[7]:


s="application"
s1="app3424"
print(s.isalpha())
print(s1.isalpha())


# In[35]:


s="Python Programming"
s1="Python"
s2="  "
print(s.istitle())
print(s.isspace())
print(s2.isspace())



# In[41]:


s1="Python"
print("a ".join(s1))


# In[44]:


print(",".join(["python","programming","easy"]))


# In[47]:


s="python programming is easy to learn"
print(s.split())
print(s.split("a"))
lst=s.split()
print(lst.index("is"))


# In[49]:


s="python programming is easy to learn"
lst= list(s)
print(lst)


# In[52]:


##replace
s="python programming"
print(s.replace("gra",'application'))


# In[55]:


t=("python","programming","1989","2019","machine learning","AI")
t1=(1,1,2,3,4)
print(t)
print(t1)


# In[63]:


t=("python","programming","1989","2019","machine learning","AI")
print("t[0]=",t[0])
print("t[1]=",t[1])
print("t[-1]=",t[-1])
print("t[1:4]=",t[1:4])
print("t[2:2]=",t[2:2])
print("t[2:-2]=",t[2:-2])


# In[66]:


t=("python","programming","1989","2019","machine learning","AI")
print(t)
t[2]=2019
del t[2]


# In[70]:


t=("python","programming","1989","2019","machine learning","AI")
del t
print(t)


# In[68]:


t=("python","programming","1989","2019","machine learning","AI")
t1=(1988,2019,"ML","AI")
t2=t+t1
print(t2)


# In[77]:


t=("python","programming","1989","2019","machine learning","AI")
t1=("python","6576","trytr")
t2=(5,454,6,2,645,1,0,45)
print(len(t))
print(len(t1))
print(max(t2))
print(min(t2))
print(cmp(t1,t2)


# In[79]:


list=["python","programming","1989","2019","machine learning","AI"]
print(list)
tuple1=tuple(list)
print(tuple1)


# In[88]:


##PYTHON--DICTIONARY
user1={"name":"anil","age":20,'emailid':'anil@gmail.com',"M.no.":917161901}
print("user1[name]=",user1['name'])
print("user1[age]=",user1["age"])
print("user1[emailid]=",user1["emailid"])
print("user1[M.no.]=",user1["M.no."])


# In[107]:


##updating of data
user1={"name":"anil","age":20,'emailid':'anil@gmail.com',"M.no.":917161901}
print(user1["age"])
user1["age"]=35
print(user1['age'])
user1["address"]="hyderabad"
print(user1)

del user1["age"]
# print(user1["age"])
# user1.clear()
user1.clear()
user1


# In[111]:


##methods in dictionary
user1={"name":"anil","age":20,'emailid':'anil@gmail.com',"M.no.":917161901}
print(user1)
user1
user1["address"]='hyd'
print(len(user1))
user1


# In[112]:


user1={"name":"anil","age":20,'emailid':'anil@gmail.com',"M.no.":917161901}
user2=user1.copy()
user2


# In[113]:


user1={"name":"anil","age":20,'emailid':'anil@gmail.com',"M.no.":917161901}
print(user1.items())


# In[114]:


user1={"name":"anil","age":20,'emailid':'anil@gmail.com',"M.no.":917161901}
user2=user1.copy()
print(user1.values())
print(user2.values())


# In[116]:


lst=["python","programming"]
print("%s %s"%(lst[0],lst[1]))


# In[121]:


lst=["python","programming"]
print("{0} {1}".format(lst[0],lst[1]))


# In[118]:


print('abcdefcdghcd'.split('cd'))


# In[122]:


##contact applications
##checking the given value is present in dictionaryr not
contacts={}
def addcontact(name,phone):
    if name not in contacts:
        contacts[name]=phone
        print("contact %s added" % name)
    else:
        print("contact %s already exists" % name)
    return
addcontact('anil',897754231)
addcontact("harsha",8341550570)
addcontact("anil",9848532542)
            


# In[127]:


##search for a particular contact from contact lists

def searchcontact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exists"% name)
    return
searchcontact('anil')
searchcontact("harsha")
searchcontact("love")
                 


# In[128]:


print(contacts)


# In[ ]:


###new contacts is given as a dictionary                                                                                         
    ##


# In[3]:


###new contacts is given as a dictionary  
###merge new contact with existing contacts list
contacts={'anil': 897754231, 'harsha': 8341550570}
def importcontacts(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added successfully")
    return
newcontacts={"dinesh":9955664637,"ajay":787656876}
importcontacts(newcontacts)
             


# In[4]:


##delete a contact from a list
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,"is deleted from the contacts")
    else:
        print(name,"is not exists in the contacts")
    return
deletecontact("harsha")
deletecontact('naveen')
    


# In[5]:


print(contacts)


# In[6]:


##modifying a contact
def updatecontact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name,": updated with new phone number")
    else:
        print(name,":not exists in contacts")
    return
updatecontact("anil",7823476784)
updatecontact("harsha",776878424)


# In[7]:


print(contacts)


# In[10]:


lst=[1,2,3,4]
print("value at : {0} value at : {1}".format(lst[0],lst[1]))
print("value at : {0} value at : {1}".format(lst[2],lst[3]))


# In[14]:


###packages and modules
from math import floor as f1
f1(123.999)


# In[16]:


from math import factorial as fact
fact(2)


# In[20]:


##generate the random no. between two limits
import random
def generaterandomnumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=' ')
    return
generaterandomnumbers(10,12,120)
             

