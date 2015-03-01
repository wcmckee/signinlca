
# coding: utf-8

# wcUsersData
# 
# Script to get users logged into the system.
# 
# Saves the output of users as the hostname of the system.
# Convert to a dict and json object, merging with other hostname output.
# 
# Runs script every min and if user is found then - time from their account 
# 
# File with, usernames, time remaining on user.
# 
# time file is a json object.
# {'username' : 'wcmckee', 'time' : 320 }
# 
# time is amount of time left on account.
# 
# script to check this object and if 0 - lock account. ELSE, allow login. 
# 
# Script to add time to acoun,, auto add time to certain groups/user a day. 
# 
# 
# 
# username 45

# In[19]:

import os
import socket
import json


# In[21]:

usertimedict = dict()


# In[24]:

lisho = os.listdir('/home')


# In[25]:

for ish in lisho:
    usertimedict.update({ish : 0})


# In[26]:

usertimedict


# In[36]:

addtime = (raw_input('add how much time: '))


# In[37]:

#letim = len(addtime)


# In[38]:

letim


# In[39]:

addtime


# In[40]:

type(addtime)


# In[42]:

intime = int(addtime)


# In[45]:

for ish in lisho:
    usertimedict.update({ish : intime})


# In[46]:

usertimedict


# In[ ]:

opus = open('/home/wcmckee/sellcoffee/hostnames', 'w')
opus


# In[5]:

myhn = socket.gethostname()


# In[6]:

myhn


# In[9]:

osscm = ('users > ' + myhn + '.txt')


# In[11]:

osscm


# In[ ]:




# In[ ]:




# In[12]:

os.chdir('/home/wcmckee/sellcoffee/')


# In[13]:

os.system(osscm)


# In[14]:

ophos = open('/home/wcmckee/sellcoffee/' + myhn + '.txt')


# In[15]:

ophos.read()


# In[17]:

ophos.close()


# In[ ]:




# In[ ]:



