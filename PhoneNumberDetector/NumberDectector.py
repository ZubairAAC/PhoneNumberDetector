#!/usr/bin/env python
# coding: utf-8

# In[2]:


import phonenumbers


# In[3]:


from phonenumbers import geocoder


# In[4]:


from phonenumbers import carrier


# In[7]:


ch_number = phonenumbers.parse("your phone number here","CH")
geocoder.description_for_number(ch_number,"en")


# In[6]:


ro_number=phonenumbers.parse("your phone number here","RO")
carrier.name_for_number(ro_number,"en")


# In[ ]:




