#!/usr/bin/env python
# coding: utf-8

# In[10]:


####File HAndling in Python
#function to creat a file and write some data
def createfile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write("this is %d line\n" % i)
    print("file is created successfully and data has been written")
    f.close()
    return
createfile("file.txt")


# In[22]:


#function for reading the file data
def readfile(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        print(x)
    f.close()
    return

readfile("file.txt")
             
             
    


# In[ ]:





# In[21]:


#data to append
#function to append the data to existing file
def appenddata(filename):
    f=open(filename,'a')
    f.write("newline 1\n")
    f.write("new line")
    return
appenddata('file.txt')


# In[11]:


ls


# In[16]:


def dataanalysiswordcount(filename,word):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split()
    count=lst.count(word)
    return count
print(dataanalysiswordcount("file.txt","rest"))


# In[16]:


#function to count of characters in the file
def countcharacter(filename):
    f=open(filename,'r')
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    return len(lst)
print(countcharacter("file.txt"))


# In[9]:


#function to count upper case characters from given file
def uppercasecount(filename):
    cntlower=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.islower():
            cntlower+=1            
    return cntlower
uppercasecount("file.txt")


# In[24]:


#function to count no. of lines
def nooflines(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split("\n")
    return len(lst)
print(nooflines("file.txt"))


# In[38]:


import re
txt = "5465533abcde"
p='[0-9]{2}[A-Z]{3}'
x = re.search(p, txt)
if x:
    print(True)
else: 
    print(False)


# In[30]:


import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


# In[43]:


#regular exprissions for indian mobile number
#validation for email id
#username@omainname.existension
import re
def phonenumbervalidate(phone):
    pattern="^[6-9][0-9]{9}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenumbervalidate(8341550570))
print(phonenumbervalidate(5182065788))


# In[50]:


#frist digit 0 case
import re
def phonenumbervalidate(phone):
    pattern="^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$"
    phone=str(phone)
    if re.match(pattern,phone):
         return True
    return False
print(phonenumbervalidate("08341550570"))
print(phonenumbervalidate('+919182065788'))
        


# In[49]:


#validate roll  no.
##15201A0501
import re
def validaterollnumber(number):
    number=str(number)
    pattern='^[1][5][2][U][1][A][0][1-9][0-6][0-9]$'
    if re.match(pattern,number):
        return True
    return False
print(validaterollnumber("152U1A0555"))
print(validaterollnumber("152U1A0485"))


# In[61]:


import re
def validateemailid(email):
    number=str(email)
    pattern="^[0-9a-z][0-9a-z .]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    return False
print(validateemailid("anil234@gmail.com"))
print(validateemailid("ukm@gmail.com"))


# In[ ]:


import re
def validatepassword(s):
    number=str(email)
    pattern="^[0-9a-z][0-9a-z .]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    return False
print(validateemailid("anil234@gmail.com"))
print(validateemailid("ukm@gmail.com"))

