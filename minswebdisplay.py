
# coding: utf-8

# Mins Web Display
# 
# Display hostname and mins data on a web site.
# 
# 

# In[29]:

import os
from datetime import datetime
import json
import dominate
#import gimpfu
 
minsfold = "/home/wcmckee/sellcoffee/mins/"
#modifiedTime = os.path.getmtime(filePath)
 
#print datetime.fromtimestamp(modifiedTime).strftime("%d%b%Y %H:%M:%S")


# In[3]:

minlis = os.listdir(minsfold)


# In[10]:

rdminz = []


# In[11]:

mindictz = dict()


# In[12]:

for minl in minlis:
    print minl
    opminza = open('/home/wcmckee/sellcoffee/mins/' + minl)
    #rdminz.append(opminza.read())
    mindictz.update({minl : opminza.read()})
    opminza.close()


# In[13]:

rdminz


# In[14]:

mindictz


# In[17]:

lshosnz = ('/home/wcmckee/sellcoffee/hostnames/')


# In[19]:

complisz = os.listdir(lshosnz)


# In[21]:

compdict = dict()


# In[28]:

json.dumps(mindictz)


# In[24]:

for compl in complisz:
    print compl
    opcompd = open(lshosnz + compl)
    compdict.update({compl:opcompd.read().replace('\n', '')})
    opcompd.close()


# In[25]:

compdict


# In[27]:

json.dumps(compdict)


# In[ ]:



