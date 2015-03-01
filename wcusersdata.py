
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

<<<<<<< HEAD
# In[5]:
=======
# In[19]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

import os
import socket
import json


<<<<<<< HEAD
# In[6]:
=======
# In[21]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

usertimedict = dict()


<<<<<<< HEAD
# In[7]:
=======
# In[24]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

lisho = os.listdir('/home')


<<<<<<< HEAD
# In[8]:
=======
# In[25]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

for ish in lisho:
    usertimedict.update({ish : 0})


<<<<<<< HEAD
# In[9]:
=======
# In[26]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

usertimedict


<<<<<<< HEAD
# In[10]:
=======
# In[36]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

addtime = (raw_input('add how much time: '))


<<<<<<< HEAD
# In[11]:
=======
# In[37]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

#letim = len(addtime)


<<<<<<< HEAD
# In[12]:

#letim


# In[13]:
=======
# In[38]:

letim


# In[39]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

addtime


<<<<<<< HEAD
# In[14]:
=======
# In[40]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

type(addtime)


<<<<<<< HEAD
# In[15]:
=======
# In[42]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

intime = int(addtime)


<<<<<<< HEAD
# In[16]:
=======
# In[45]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

for ish in lisho:
    usertimedict.update({ish : intime})


<<<<<<< HEAD
# In[17]:
=======
# In[46]:
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad

usertimedict


<<<<<<< HEAD
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
=======
# In[ ]:

opus = open('/home/wcmckee/sellcoffee/hostnames', 'w')
opus


# In[5]:

myhn = socket.gethostname()


# In[6]:

myhn
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad


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

<<<<<<< HEAD
print ophos.read()
=======
ophos.read()
>>>>>>> 7a6b9af1a7e9e9fedd7ff3b78f3248c1262d27ad


# In[17]:

ophos.close()


# In[ ]:




# In[ ]:



