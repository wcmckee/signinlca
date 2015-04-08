
# coding: utf-8

# Account Loop Ping 
# 
# Script that adds time.
# 
# Script that get all the users on the system, sets their mins.

# In[16]:

import os
import json
import socket


# In[17]:

myhn = socket.gethostname()


# In[18]:

myhn


# In[18]:




# In[19]:

lisho = os.listdir('/home')


# In[20]:

lisho


# In[21]:

usertimdict = dict()


# In[22]:

for ish in lisho:
    usertimdict.update({ish : 0})


# In[23]:

jstim  = json.dumps(usertimdict)


# In[24]:

jstim


# In[25]:

opus = open('/home/wcmckee/sellcoffee/hostnames/' + myhn, 'w')

opus.write(jstim)

opus.close()


# In[25]:




# In[ ]:



