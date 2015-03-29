
# coding: utf-8

# In[2]:

#check username for minutes file. minutes file is the amount of
#mins on username.

#script that runs every min to add time to all accounts
#that are logged on.


# In[1]:

import os


# In[2]:

allusr = os.listdir('/home')


# In[3]:

allusr

usrslcd = ('/home/wcmckee/signinlca/usernames/')


# In[4]:

#write a file in the home folder of each user that 
#is the amount of mins they used.

#dict of usernames: mins loged on



# In[5]:

usrdict = dict()


# In[6]:

usrdict


# In[7]:

hostndir = ('/home/wcmckee/sellcoffee/hostnames/')


# In[8]:

hosnz = os.listdir(hostndir)


# In[9]:

for hosz in hosnz:
    print hosz
    hopen = open(hostndir + hosz, 'r')
    usrdict.update({hosz : hopen.read().strip('\n')})
    hopen.close()


# In[10]:

totlis = []


# In[11]:

for usrval in usrdict.values():
    totlis.append(usrval.split())
    #print usrval.replace(' ', ', ')
    #totlis.append(usrval.replace(' ', ''))
    #for uza in usrval:
        #if 'w' in uza:
            #print 'w there!'
        #else:
            #print ('w not there!')
        #print uza


# In[12]:

totlis


# In[13]:

for totz in totlis:
    #print totz
    for tot in totz:
        print (tot)
        addminz = open(usrslcd + tot + '/minutes', 'r')
        curtim = addminz.read()
        addminz.close()
        newminz = open(usrslcd + tot + '/minutes', 'w')
        topminz = int(curtim) + 1
        newminz.write(str(topminz))
        newminz.close()
        #str of user loged on. if name is here then
        #edit minutes folder with +1 min


# In[13]:




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



