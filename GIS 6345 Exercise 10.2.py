#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cumsum(t):
    t = [1, 2, 3]
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res


# In[2]:


print (cumsum)


# In[3]:


def cumulative(l):
    cumulative_sum = 0


# In[4]:


def cumulative(t):
    cumulative_sum = 0
    new_list = [1, 2, 3]
    for i in t:
        cumulative_sum += i
        new_list.append(cumulative_sum)
    return new_list


# In[5]:


print (cumulative)


# In[6]:


def Cumulative(l):
    new = []
    cumsum = 0
    for element in l:
        cumsum += element
        new.append(cumsum)
    return new


# In[7]:


lists = [1, 2, 3]


# In[8]:


print (New list:,Cumulative(lists))


# In[9]:


def Cumulative(l):
    new = [1, 3, 6]
    cumsum = 0
    for element in l:
        cumsum += element
        new.append(cumsum)
    return new


# In[10]:


lists = [1, 2, 3]


# In[11]:


print (New list:,Cumulative(lists))


# In[ ]:




