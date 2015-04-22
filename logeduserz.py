
# coding: utf-8

# script that sends users logged in data from a folder. Folder contains all the hostnames and their users logged in. 
# 
# Really what I want generated is a json file containing every hostname and userslogged in.

# In[28]:

import os


# In[29]:

os.system('rsync -azP wcmckee@192.168.1.2:/home/wcmckee/sellcoffee/ /home/wcmckee/sellcoffee/')


# In[30]:

mylis = os.listdir('/home/wcmckee/sellcoffee/hostnames/')


# In[31]:

jsdict = dict()


# In[ ]:




# In[32]:

for lis in mylis:
    print lis
    rdhos = open('/home/wcmckee/sellcoffee/hostnames/' + lis, 'r')
    hosrdz = rdhos.read()
    jsdict.update({lis: hosrdz})


# In[ ]:

jsdict


# In[34]:

jsdict.keys()[0]


# In[35]:

jsdict.values()[0]


# In[36]:

jsdict.keys()[1]


# In[37]:

jsdict.values()[1]


# In[38]:

jsdict.keys()[2]


# In[39]:

jsdict.keys()[3]


# In[42]:

jsdict.values()[2]


# In[43]:

jsdict.values()[3]


# In[ ]:



