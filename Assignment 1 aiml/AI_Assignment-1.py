#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Show that a List in python can
• store elements of different types (integer, float, string, etc.)
• store duplicate elements """
lst=[1,'A',"String",1.1,-2]
print(lst)


# In[3]:


#Check if an Element Exists in a List ( Note make use of ‘in’)
num=[1,2,3,4,5]
n=int(input("Enter a number:"))
if n in num:
    print("Element present")
else:
    print("Element not present")


# In[4]:


#Find the length of the list
lst=[1.2,3,0,-4,'f']
print(len(lst))


# In[8]:


#Create a list with value n ** 2 where n is a number from 1 to 5
lst=[]
for i in range(1,5):
   lst.append(i**2)
print(lst)


# In[9]:


#Python program to print the elements of an array in reverse order
print(lst[::-1])


# In[12]:


#Python program to sort the elements of an array in descending order
array=[1,4,5,7,3]
array.sort(reverse=True)
print(array)


# In[29]:


""""Compare 2 lists in python(use The cmp() function
• The set() function and == operator
• The sort() function and == operator)"""
list1=[2,3,4,5,5,1,1]
list2=[2,3,4,5,5,1,1]
(list1.sort(reverse=False))
(list2.sort(reverse=False))
print(list1)
print(list2)
if list1==list2:
    print("Equal")
else:
    print("Not equal")
n1=set(list1)
n2=set(list2)
print(n1)
print(n2)


# In[28]:


#Remove a specific item from a list by using the three methods remove(), pop() and clear().
lst=[1,'a',2.2,0,-9]
lst.remove(1)
lst.pop()
print(lst)
lst.clear()
print(lst)


# In[31]:


"""Write a NumPy program to convert an integer array to a floating type.
( x = np.asfarray(a))"""
import numpy as np
arr=np.array([1,2,3])
print(arr)
x=np.asfarray(arr)
print(x)


# In[34]:


#Write a NumPy program to convert a list and tuple into arrays. 
import numpy as np
lst=[1.1,2.2,3.3]
tple=(1,2,3)
x=np.array(lst)
y=np.array(tple)
print(x)
print(type(x))
print(y)


# In[35]:


#Write a NumPy program to convert a list and tuple into arrays.(np.asarray)
import numpy as np
lst=[1.1,2.2,3.3]
tple=(1,2,3)
x=np.asarray(lst)
y=np.asarray(tple)
print(x)
print(type(x))
print(y)


# In[ ]:




