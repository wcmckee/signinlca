
# coding: utf-8

# Affect Account
# 
# Script that causes affects to users when the minutes folder reaches a certain amount.
# 
# Read minutes folder. If user has less than 10 mins warn them. At 5 mins warn every 5 mins. 10 seconds count down. 
# Suggest they buy more time. 

# minlim is a file called username-minlim. It contains a int that is the max amount of mins that user is allowed. 
# 
# If the user reaches their limit - they are loged out. 

# In[3]:

import os


# In[ ]:




# In[1]:

minlimf = ('/home/wcmckee/sellcoffee/minlim/')


# In[9]:

rdminz = ('/home/wcmckee/sellcoffee/mins/')


# In[10]:

lshom = os.listdir(rdminz)


# In[11]:

lshom


# In[15]:

for lsh in lshom:
    print lsh
    opminz = open(minlimf + lsh, 'w')
    #Here i write the limit that all users will be getting.
    #Change this file for indivials/groups etc. 
    opminz.write(str(60))
    opminz.close()


# In[18]:

for lsh in lshom:
    #print lsh
    opminz = open(rdminz + lsh, 'r')
    #Here i write the limit that all users will be getting.
    #Change this file for indivials/groups etc. 
    opminz.read()
    opminz.close()


# In[13]:

minlimf


# In[7]:

rdminz


# In[9]:

usrdir = os.listdir(rdminz)


# In[10]:

#Make folders of usersnames from /home in /signinlca/usernames
#make username-time etc files


# In[11]:

minz = ('/home/wcmckee/sellcoffee/usernames/')


# In[12]:

os.listdir(minz)


# In[18]:

thrlis = []


# In[ ]:




# In[13]:

holis = os.listdir('/home')


# In[20]:

for hol in holis:
    #print hol
    #print hol.upper()
    
    hthr = hol.replace('b', '3')
    print hthr
    thrlis.append(hthr)
    #for usrd in usrdir:
    #    if hol == usrd:
            #print('its correct!')
    #        print hol
    #    else:
    #        print hol
    #        print('its not correct :(!')

#compare two lists - home and usernames. if home item isnt in 
#username item - add it make folder/files etc.


# In[21]:

thrlis


# In[ ]:




# In[16]:

hthr


# In[ ]:




# In[14]:




# In[ ]:



