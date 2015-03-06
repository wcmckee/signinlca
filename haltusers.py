
# coding: utf-8

# Halt Users
# 
# Halt there users!
# 
# Stop and starts user stuff

# In[1]:

import os


# In[2]:

#Make it easy to check on local pi/debian computers. 
#List of everyone logged on and what machine they are logged 
#into.

#Hostname id is last three/two characters of ip address.


# In[3]:

hostndir = ('/home/wcmckee/sellcoffee/hostnames/')


# In[4]:

os.listdir(hostndir)


# In[5]:

chosd = os.chdir(hostndir)


# In[15]:

os.system('hostname > host.txt')


# In[11]:

rdhos = open('host.txt', 'r')

rdtxt = rdhos.read()

rdhos.close()


# In[13]:

rdstp = rdtxt.strip('\n')


# In[14]:

rdstp


# In[ ]:




# In[16]:

os.system('users > ' + rdstp)


# In[ ]:

os.system('rm -rf host.txt')


# In[20]:

whatip = raw_input('What ip address to rsync to: ')

whaint = int(whatip)


# In[22]:

os.system('rsync -azP /home/wcmckee/sellcoffee/ wcmckee@192.168.1.' + str(whaint) +':/home/wcmckee/sellcoffee')


# In[24]:

os.system('rsync -azP /home/wcmckee/github/ wcmckee@192.168.1.' + str(whaint) + ':/home/wcmckee/github/')


# In[ ]:



