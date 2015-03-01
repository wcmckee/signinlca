
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

# In[5]:

import os
import socket
import json


# In[6]:

usertimedict = dict()


# In[7]:

lisho = os.listdir('/home')


# In[8]:

for ish in lisho:
    usertimedict.update({ish : 0})


# In[9]:

usertimedict


# In[10]:

addtime = (raw_input('add how much time: '))


# In[11]:

#letim = len(addtime)


# In[12]:

#letim


# In[13]:

addtime


# In[14]:

type(addtime)


# In[15]:

intime = int(addtime)


# In[16]:

for ish in lisho:
    usertimedict.update({ish : intime})


# In[17]:

usertimedict


# In[19]:

myhn = socket.gethostname()


# In[37]:

#Edit just one person

edione = raw_input('Which user to edit time: ')
timedi = raw_input('How much time to add: ')

usertimedict.update({edione : timedi})


# In[20]:

jstim = json.dumps(usertimedict)


# In[21]:

jstim


# In[24]:

opus = open('/home/wcmckee/sellcoffee/hostnames/' + myhn, 'w')

opus.write(jstim)
opus.close()


# In[26]:

rdopuw = open('/home/wcmckee/sellcoffee/hostnames/localhost', 'r')

print rdopuw.read()


# In[33]:

edione


# In[34]:

limedi = int(timedi)


# In[35]:

limedi


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

print ophos.read()


# In[17]:

ophos.close()


# In[ ]:




# In[ ]:



