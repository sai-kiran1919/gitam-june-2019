#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('hello')


# In[6]:


x=10
if(x<15):
 print("the number is less than 15")


# In[21]:


x=10
if(x>15):
 print("hello")
else:
 print("gud mrng")


# In[22]:


x= int(input("enter the nuymber"))
print(x)


# In[23]:


x=int(input("enter x value"))
y=int(input("enter y value"))
if(x>y):
    print("x is greatest")
else:
    print("y is greatest")
 


# In[27]:


x=int(input("enter x value"))
y=int(input("enter y value"))
if(x==y):
    print(x*x)
else:
    print(x*y)


# In[28]:


x=10
if(x<0):
    print(" x is negative")
elif(x>0):
    print("x is positive")
elif(x==0):
    print("x is zero")


# In[31]:


n=0
while(n<=10):
    print(n)
    n=n+1


# In[2]:


n=10
while(n>=0):
    print(n)
    n=n-1


# In[4]:


x=1
y=100
sum=0
while(x<=y):
    if(x%2==0):
        sum=sum+x
    x=x+1
    
print(sum)
    


# In[7]:


x=int(input("enter x value"))
while(x!=0):
    r=x%10
    print(r) 
    x=x//10


# In[14]:


x= 1423
print (x)


# In[19]:


y="123"[::-1]
print(y)


# In[22]:


n=145
rv=0
while(n>0):
    dig=n%10
    rv=rv*10+dig
    n=n//10
print("revrse of number", rv)


# In[6]:


x=int(input("enter the number"))
sum=0
while(x!=0):
    rev=x%10
    if(rev%2==0):
        sum=sum+rev
    x=x//10
print(sum)
    


# In[24]:


x=int(input("enter the number"))
while(x!=0):
    rev=x%10
    
    if(rev==0):
        print("zero")
    elif(rev==1):
        print("one")
    elif(rev==2):
        print("two")
    elif(rev==3):
        print("three")
    elif(rev==4):
        print("four")
    elif(rev==5):
        print("five")
    elif(rev==6):
        print("six")
    elif(rev==7):
        print('seven')
    elif(rev==8):
        print("eight")
    elif(rev==9):
        print("nine")
    x=x//10
    


# In[2]:


n=int(input("enter n value"))
l1=int(input("enter n1 value"))
l2=int(input("enter n2 value"))
count=0
while(l1!=l2):
    temp=l1
    r=l1%10
    if(r==n):
        count=count+1
    l1=l1//10
    l1=b=temp
    l1=l1+1
print(count)


# In[9]:


def printnnaturalnumbers(n):
    cnt=1
    while(cnt<=n):
        print(cnt)
        cnt=cnt+1
    print()
    return
printnnaturalnumbers(9)
printnnaturalnumbers(30)


# In[17]:


def printnnaturalnumbers(n):
    cnt=1
    while(cnt<=n):
        print(cnt,end="  ")
        cnt=cnt+1
    
print(printnnaturalnumbers(9))
print(printnnaturalnumbers(30))


# In[18]:


def findfact(n):
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    print(fact)
findfact(5)
findfact(9)


# In[11]:


def countpallindrome(n1,n2):
    cnt=0
    while(n1!=n2):
        sum=0
        buffer=n1
        while(n1!=0):
            r=n1%10
            sum=(sum*10)+r
            n1=n1//10
        if(buffer==sum):
            count=count+1
        n1=buffer
        n1=n1+1
    return count
print(countpallindrome(10,30))

        
    
    
    
    


# In[ ]:




