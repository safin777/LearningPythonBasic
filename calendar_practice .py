#!/usr/bin/env python
# coding: utf-8

# In[28]:


import calendar as cal


# In[29]:


print (cal.month(2019,3))
print ()


# In[30]:


print (cal.calendar(2020))


# In[31]:


leap= cal.isleap(2020)
print("2020 is leap year is",leap)
#find out leap year from the entire data


# In[32]:


how_many_leap_days = cal.leapdays(2018,2022)
print (how_many_leap_days)
#counting leap days for a range of years


# In[ ]:




