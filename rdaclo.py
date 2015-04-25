
# coding: utf-8

# rdaclo
# 
# read account loop
# 
# Script that does things depending on how much time the user has. Reads time file that is a dict with key of user and value is time
# 
# This script adds +1 to each user logged into a system.
# 
# This is the client machine - all slaves get their data sent to this.
# This script should run every min on the client machine. 

# In[29]:

import json
import os
#import configparser
import socket
myhosn = socket.gethostname()

import dominate
from dominate.tags import * 


# In[ ]:




# In[2]:

#rdmins


# In[3]:

intres = []


# In[4]:

curmins = dict()


# In[5]:

#for rdm in rdmins:
    #print rdm
    #rdmz = open('/home/wcmckee/sellcoffee/mins/' + rdm, 'r')
    #print rdmz.read()
    #intres.append(rdmz.read())
    #curmins.update({rdm: rdmz.read()})
    #rdmz.close()
    #nexnum = int(rdmz.read() + 1)
    #print int(1) + int(5)


# In[6]:

#curmins


# In[ ]:




# In[7]:

#intres


# In[8]:

holisz = os.listdir('/home/wcmckee/sellcoffee/hostnames/')


# In[9]:

#holisz


# In[10]:

develist = []
os.listdir('/home/wcmckee/sellcoffee/usernames/')


# In[11]:

rdhoszr = open('/home/wcmckee/sellcoffee/usernames/' + myhosn + '-minutes', 'r')
tesred = rdhoszr.read()
develist.append(str(tesred))
rdhoszr.close()

    


# In[12]:

#for curmiz in curmins:
    #print curmiz
    #if  in curmiz:
# #       print cuz


# In[13]:

for deusr in develist:
    print deusr
    #rdmz = open('/home/wcmckee/sellcoffee/mins/' + deusr, 'w')
    #rdmz.write()
    


# In[14]:

#rdhoszr = open('/home/wcmckee/sellcoffee/hostnames/' + )


# In[15]:

for intr in intres:
    print int(intr) + 1


# In[16]:

allhost = os.listdir('/home/wcmckee/sellcoffee/hostnames/')


# In[17]:

usrzlogd = []
usrdict = dict()


# In[18]:

for alhos in allhost:
    print alhos
    rdza = open('/home/wcmckee/sellcoffee/hostnames/' + alhos, 'r')
    usrzlogd.append(rdza.read().replace('\n', ''))
    
    


# In[19]:

rdza.close()


# In[20]:

for alhos in allhost:
    print alhos
    rdza = open('/home/wcmckee/sellcoffee/hostnames/' + alhos, 'r')
    usrdict.update({alhos : rdza.read().replace('\n', '').split()})
    
    


# In[21]:

usrzlogz = usrdict.values()


# In[22]:

thusrz = []
chedct = dict()
usrzlogedin = []


# In[23]:

#usrdict
#The lists of each computer only need 


# In[24]:

myhosn = socket.gethostname()


# In[25]:

#Checks users logged on to local machine and add 1 min to 
rdmins = os.listdir('/home/wcmckee/sellcoffee/mins/')


#if their name is shown on list open sellcoffee/mins + the username
#that is show. add + 1 to the number.


# In[26]:

#checks users logged on and if user is logged on the add 1 min to
#their name in mins folder.
    
rdmz = open('/home/wcmckee/sellcoffee/mins/' + myhosn, 'w')
for intr in intres:
    print int(intr) + 1
    rdmz.write(str(int(intr) + 1))


# In[27]:

usrdict


# In[35]:

for usrza in usrdict.values():
    seusr = set(usrza)
    #print list(seusr)
    strsrtr = list(seusr)
    for strz in strsrtr:
        print strz
        oplocaz = open('/home/wcmckee/sellcoffee/mins/' + strz, 'r')
        oprdza = oplocaz.read()
        print oprdza
        newnum = int(oprdza) + 1
        opediza = open('/home/wcmckee/sellcoffee/mins/' + strz, 'w')
        opediza.write(str(newnum))
        opediza.close()
        
        #for rdm in rdmins:
           # print rdm
            
        usrzlogedin.append(strz)
        #chedct.update({usrdict.keys() : strz})
        


# In[34]:

for usrzl in usrzlogedin:
    print usrzl


# In[201]:

#chdict.update()


# In[71]:

#usrslogedindic = dict()


# In[75]:

#for usrva in usrdict.values():
    #print usrva
    #for usrv in usrva:
        #print usrv
        #cycles though printing out each user loged in. 
        #I want to add one min to their name if their name 
        #shows up here. 
        #create a dict that is
        #{username : +1 (number increases their 
        #loged in on multimachines)}


# In[74]:

#usrslogedindic


# In[7]:

#opus = open('/home/wcmckee/sellcoffee/hostnames/localhost', 'r')


# In[8]:

#opjsn = opus.read()


# In[9]:

#neza = json.loads(opjsn)


# In[15]:

#os.system('sudo passwd -l ' + locusa) 
#os.system('sudo pgrep -u ' + locusa)
#os.system('sudo killall -KILL -u ' + locusa)neza.keys()


# In[23]:

#neza#


# In[33]:

#for nezf in neza.values():
   # print nezf
    #if nezf == 0:
        #print ('No Time!')
        #print ('Logout ' + neza())


# In[40]:

#for naez in neza.keys():
    #print naez


# In[38]:

#for nezf in neza.values():
    #print nezf
    #if nezf == 0:
        #print ('No Time!')
        #print ('Logout ' + neza())
        


# Write a config file that has each user and their time. 

# In[43]:

#config = configparser.RawConfigParser()


# In[44]:

#config.read('/home/wcmckee/signinlca/usertime.cfg')


# In[45]:

#config.add_section('users')


# In[46]:

#for naez in neza.keys():
    #print naez
    #config.set('users', naez, 0)


# In[48]:

#with open('/home/wcmckee/signinlca/users.cfg', 'wb') as configfile:
    #config.write(configfile)


# In[ ]:



