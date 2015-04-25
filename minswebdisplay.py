
# coding: utf-8

# Mins Web Display
# 
# Display hostname and mins data on a web site.
# 
# 

# In[18]:

import os
from datetime import datetime
import json
import dominate
#import gimpfu
 
minsfold = "/home/wcmckee/sellcoffee/mins/"
#modifiedTime = os.path.getmtime(filePath)
 
#print datetime.fromtimestamp(modifiedTime).strftime("%d%b%Y %H:%M:%S")


# In[19]:

minlis = os.listdir(minsfold)


# In[20]:

rdminz = []


# In[21]:

mindictz = dict()


# In[22]:

for minl in minlis:
    print minl
    opminza = open('/home/wcmckee/sellcoffee/mins/' + minl)
    #rdminz.append(opminza.read())
    mindictz.update({minl : opminza.read()})
    opminza.close()


# In[23]:

rdminz


# In[24]:

mindictz


# In[25]:

lshosnz = ('/home/wcmckee/sellcoffee/hostnames/')


# In[26]:

complisz = os.listdir(lshosnz)


# In[27]:

compdict = dict()


# In[30]:

minjson = json.dumps(mindictz)


# In[32]:

savjsmin = open('/home/wcmckee/sellcoffee/minutes.json', 'w')

savjsmin.write(minjson)


# In[33]:

savjsmin.close()


# In[29]:

for compl in complisz:
    print compl
    opcompd = open(lshosnz + compl)
    compdict.update({compl:opcompd.read().replace('\n', '')})
    opcompd.close()


# In[17]:




# In[34]:

compjsq = json.dumps(compdict)


# In[35]:

savjsnusr = open('/home/wcmckee/sellcoffee/comps.json', 'w')

savjsnusr.write(compjsq)

savjsnusr.close()


# In[36]:

rdcompz = open('/home/wcmckee/sellcoffee/comps.json', 'r')

rdstrza = rdcompz.read()


# In[37]:

rdstrza


# In[ ]:



