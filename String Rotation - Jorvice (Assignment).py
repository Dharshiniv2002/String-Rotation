#!/usr/bin/env python
# coding: utf-8

# In[4]:


def findRotations(str1, str2):
    x = 0
    y = 0
    m = str1
     
    while True:
        m = m[len(m)-1] + m[:len(m)-1]

        if(m == str2):
            x += 1
            break
             
        else:
            x += 1
            if x > len(str2) :
                break
  
    while True:
        str1 = str1[1:len(str1)]+str1[0]
        if(str1 == str2):
            y += 1
            break
             
        else:
            y += 1
            if y > len(str2):
                break
                 
    if x < len(str2):
        print(min(x,y))
         
    else:
        print("given strings are not of same kind")
findRotations('orvicej', 'jorvice')


# Explanation: j is rotated left to obtain jorvice.
# 

# In[3]:


def findRotations(str1, str2):
    x = 0
    y = 0
    m = str1
     
    while True:
        m = m[len(m)-1] + m[:len(m)-1]

        if(m == str2):
            x += 1
            break
             
        else:
            x += 1
            if x > len(str2) :
                break
  
    while True:
        str1 = str1[1:len(str1)]+str1[0]
        if(str1 == str2):
            y += 1
            break
             
        else:
            y += 1
            if y > len(str2):
                break
                 
    if x < len(str2):
        print(min(x,y))
         
    else:
        print("given strings are not of same kind")
findRotations('rvicejo', 'jorvice')


# o and j are left rotated to obtain jorvice.
