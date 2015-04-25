
# coding: utf-8

# In[13]:

#check username for minutes file. minutes file is the amount of
#mins on username.

#script that runs every min to add time to all accounts
#that are logged on.

#Script that resets mins to zero!


# In[28]:

import os


# In[29]:

allusr = os.listdir('/home')


# In[30]:

#print allusr

usrslcd = ('/home/wcmckee/sellcoffee/usernames/')


# In[31]:

minsfil = ('/home/wcmckee/sellcoffee/mins/')


# In[32]:

for usfc in allusr:
    #print usfc
    opmin = open('/home/wcmckee/sellcoffee/mins/' + usfc, 'w')
    opmin.write(str(0))
    print (usfc + ' mins reset to zero')
    opmin.close()


# In[5]:

#write a file in the home folder of each user that 
#is the amount of mins they used.

#dict of usernames: mins loged on



# In[14]:

#rsetmin = raw_input('Reset minutes to 0? y/n ')

#if 'y' in rsetmin:
#    for alu in allusr:
#        print alu
#        mktimfold = open(usrslcd + alu + '/minutes', 'w')
#        mktimfold.write('0')
#        mktimfold.close()


# In[15]:




# In[15]:




# In[ ]:



