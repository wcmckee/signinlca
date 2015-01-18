
# coding: utf-8

# signinlca
# 
# script to signin for volunteers at lca2015
# 
# test!

# In[29]:

import os
import time
import json
import getpass


# In[30]:

def returndate():
    return time.strftime(("%d" + "-" + "%b" + "-" + "%Y"))

def returntime():
    return time.strftime("%H:%M:%S")


# In[31]:

firnam = raw_input('first name: ')
lasnam = raw_input('last name: ')
tshir = raw_input('tshirt size: ')
cofvol = raw_input('coffee volc: ')
comen = raw_input('comments: ')


# In[32]:

betdict = dict()


# In[33]:

betdict.update({'first-name' : firnam})
betdict.update({'last-name' : lasnam})
betdict.update({'signin-date' : returndate()})
betdict.update({'signin-hrmin' : returntime()})
betdict.update({'tshirt-size' : tshir})
betdict.update({'coffees' : int(cofvol)})
betdict.update({'comments:' : comen})


# In[34]:

betdict


# In[35]:

convj = json.dumps(betdict)


# In[36]:

convj


# In[37]:

puser = getpass.getuser()


# Current path is wcmckee@localhost:~/signinlca/18/Jan/2015$
# This is backwards and should be ~/signinlca/2015/Jan/18.
# 
# make path /home/user/signinlca/2015 (year)
# 
# make path /home/user/signinlca/Jan (month)
# 
# make path /home/user/signinlca/18 (day)

# In[38]:

time.strftime("%Y") #This is the year

time.strftime("%d") #This is the day

time.strftime("%b") #This is the month


# In[39]:

yrnum = time.strftime("%Y")
mnthnum = time.strftime("%b")
dayzum = time.strftime("%d")


# In[40]:

signpath = ('/home/' + puser + '/signinlca')
yrpath = (signpath + '/' + yrnum)
mnthpath = (yrpath + '/' + mnthnum)
dayzpath = (mnthpath + '/' + dayzum)


# In[41]:

yrpath


# In[42]:

if os.path.isdir(signpath) == True:
    print 'Path is there'
else:
    print 'Path not there'
    os.mkdir(signpath)


# In[43]:

if os.path.isdir(yrpath) == True:
    print 'Year Path is there'
else:
    print 'Year Path not there'
    os.mkdir(yrpath)
    
if os.path.isdir(mnthpath) == True:
    print 'Month Path is there'
else:
    print 'Month Path not there'
    os.mkdir(mnthpath)
    
if os.path.isdir(dayzpath) == True:
    print 'Day Path is there'
else:
    print 'Day Path not there'
    os.mkdir(dayzpath)


# In[43]:




# In[44]:

os.chdir(dayzpath)


# In[45]:

opday = open((firnam + lasnam) + '.json', 'w')


# In[48]:

opday.write(str(convj))
opday.close()


# In[49]:

convj


# In[47]:




# In[47]:




# In[ ]:




# In[ ]:



