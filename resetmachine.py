
# coding: utf-8

# In[106]:

#check username for minutes file. minutes file is the amount of
#mins on username.

#script that runs every min to add time to all accounts
#that are logged on.


# In[107]:

import os


# In[108]:

allusr = os.listdir('/home')


# In[109]:

allusr

usrslcd = ('/home/wcmckee/signinlca/usernames/')


# In[110]:

#write a file in the home folder of each user that 
#is the amount of mins they used.

#dict of usernames: mins loged on



# In[111]:

usrdict = dict()


# In[112]:

usrdict


# In[113]:

hostndir = ('/home/wcmckee/sellcoffee/hostnames/')


# In[114]:

hosnz = os.listdir(hostndir)


# In[115]:

for hosz in hosnz:
    print hosz
    hopen = open(hostndir + hosz, 'r')
    usrdict.update({hosz : hopen.read().strip('\n')})
    hopen.close()


# In[116]:

for usz in usrdict.values():
    newgz = usz.split()
    #print newgz
    for ussa in newgz:
        print ussa
        if ('wcmckee') in ussa:
            print ('wcmckee logged in')
        else:
            print ('not logged in!')


# In[117]:

#newgz


# In[ ]:




# In[118]:

totlis = []


# In[119]:

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


# In[ ]:




# In[132]:

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


# In[ ]:




# In[121]:

for alu in allusr:
    
    print alu
    mktimfold = open(usrslcd + alu + '/minutes', 'w')
    mktimfold.write('0')
    mktimfold.close()

