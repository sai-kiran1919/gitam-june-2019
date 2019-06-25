#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func(x=1,y=2):
    x=x+y
    y+=1
    print(x,y)
func(y=2,x=1)


# In[8]:


def printeven(n):
    cnt=0
    sum=0
    while(cnt!=n):
        if(cnt%2==0):
            sum=sum+cnt
        cnt=cnt+1
    return sum

print(printeven(20))


# In[9]:


def factorslist(n):
    i=1
    while(i!=n):
        if(n%i==0):
            print(i,end=" ")
        i=i+1
        
factorslist(12)


# In[14]:


for i in range(5*5,10**10):
    print (i)
    


# In[57]:


list1=[1,2,3,4,5,6,7]
for x in list1:
    print(x,end=" ")
print()
print(list1[4])
print(list1[3:6])
print(list1[0:3])
print(list1[:3])
print(list1[:7])
print(list1[0:7])
print(list1[2:-2])
print(list1[::2])
print(list1[::3])
print(list1[::-2])
print(list1[-1])   


# In[ ]:





# In[64]:


list1=["gwsj","jkhws",2]
list2=[3,4,5,6]
list1[1]='gitam'
print(list1)
list1[2]="rr"
print(list1)
del list1[2]
print(list1)

print(list1+list2)
print(len(list1))
print(len(list2))
list1.append(15)
list1.append(1)
list1.append(1)
list1.append(1)
print(list1)
print(list1.count(1))
list1.append([5,6,7])
print(list1)


# In[61]:


names=["amir","barry",'chales',"dao"]
print(names[[-1][-1]])
loc=names.index("edward")
print(loc)


# In[78]:


list1=["gitam","python",1,5,"python","python"]
print(list1)
list1.index('python')
list1.index(1)
print(list1)
list1.insert(4,2020)
print(list1)
list1.remove("python")
print(list1)
list1.reverse()
print(list1)


# In[80]:


list1=["gitam","python",1,5,"python","python"]
print(list1)
list1.index("python")
print(list1)


# In[ ]:





# In[89]:


def ls(n,taritem):
    flag=0
    for i in range(len(a)):
        if a[i]==taritem:
            flag=1
            break
    if(flag!=0):
        print("target item is found")
    else:
        print("targrt item is not found")

a=[16,2,12,6,9,7,1]
ls(a,6)
ls(a,12)
    


# In[85]:


def  lsduplicate(a,taritem):
    flag=0
    for i in range(len(a)):
        if(a[i]==taritem):
            flag=flag+1
    print(flag)

a=[9,1,6,1,5,9,15,15]
lsduplicate(a,9)


# In[92]:


def lexample(a,taritem):
 
    for i in range(len(a)):
        if(a[i]==taritem):
            print(i,end=" ")
a=[1,2,3,4,5,6,3]
lexample(a,3)
                  


# In[97]:


def linearexample2(a,taritem):
    for i in range(len(a)):
        if a[i]==taritem:
            j=0
            while(j!=i+1):
                print("!",end=" ")
                j=j+1
            print(end=" ")
            
a=[1,5,9,6,5,15,12,5]
linearexample2(a,15)


# In[98]:


def mul(a):
    sum=0
    for i in range(len(a)):
        if(a[i]%3==0 and a[i]%5==0):
            sum=sum+a[i]
    return sum
a=[30,12,2,9,18,36,20,45]
print(mul(a))


# In[99]:


def linearformattedoutput(a):
    for i in range(len(a)):
        if(i==0 or i==len(a)-1):
            print(a[i],end=" ")
        elif(a[i-1]%2==0 and a[i+1]%2==0):
            print(a[i],end=" ")
            
a=[1,6,9,4,16,19,22]
linearformattedoutput(a)


# In[104]:


def numbertolistconvertion(n):
    list=[]
    while(n!=0):
        r=n%10
        list.append(r)
        n=n//10
    list.reverse()
    print(list)
    
n=int(input("enter the number"))
numbertolistconvertion(n)

