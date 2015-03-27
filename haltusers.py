
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


# In[6]:

os.system('hostname > host.txt')


# In[7]:

rdhos = open('host.txt', 'r')

rdtxt = rdhos.read()

rdhos.close()


# In[8]:

rdstp = rdtxt.strip('\n')


# In[9]:

rdstp


# In[9]:




# In[10]:

os.system('users > ' + rdstp)


# In[11]:

os.system('rm -rf host.txt')


# In[ ]:

print ('script success')


# In[12]:

#whatip = raw_input('What ip address to rsync to: ')

#whaint = int(whatip)


# In[13]:

#os.system('rsync -azP /home/wcmckee/sellcoffee/ wcmckee@192.168.1.2:/home/wcmckee/sellcoffee/')


# In[14]:

#os.system('rsync -azP /home/wcmckee/signinlca/ wcmckee@192.168.1.2:/home/wcmckee/signinlca/')


# In[15]:

#os.system('rsync -azP /home/wcmckee/github/ wcmckee@192.168.1.2:/home/wcmckee/github/')


# In[ ]:



