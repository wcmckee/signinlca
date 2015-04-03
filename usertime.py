
# coding: utf-8

# Usertime
# 
# Script to help with tracking time of users logged into system. 
# 
# 

# In[11]:

import os
import getpass


# In[ ]:




# In[5]:

getusr = getpass.getuser()


# In[6]:

getusr


# In[7]:

hostndir = ('/home/' + getusr + '/sellcoffee/hostnames/')


# In[12]:

hostndir


# In[13]:

chosd = os.chdir(hostndir)


# In[14]:

chosd


# In[ ]:




# In[15]:

os.system('hostname > host.txt')

rdhos = open('host.txt', 'r')

rdtxt = rdhos.read()

rdhos.close()

rdstp = rdtxt.strip('\n')


# In[16]:

rdstp


# In[17]:

os.system('users > ' + rdstp)


# In[19]:

os.system('rm -rf host.txt')


# In[20]:

print ('script success')


# In[ ]:



