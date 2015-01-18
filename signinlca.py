
# coding: utf-8

# signinlca
# 
# script to signin for volunteers at lca2015
# 
# test!
# 
# The script asks for input of firstname, lastname, tshirt size, amount of coffee volc and comments. 
# It creates a python dict with this data along with the current date and hour. 
# It gets the username of user and saves the data in the users home dir under the folder signinlca. 
# It saves the data as a json object.
# Currently saves the file as firstname + lastname. Could this be improved?
# 
# 
# TODO
# 
# add option to choose to login or logout. Y/N option for each one. 
# 
# add logout script that appends to the login data. saves, time/date/comment. anything else?
# 
# Asign to jobs/room?
# 
# Graph up total hour worked in day/week
# 
# scp/rsync data to server/web page.
# 

# In[71]:

import os
import time
import json
import getpass


# In[72]:

def returndate():
    return time.strftime(("%d" + "-" + "%b" + "-" + "%Y"))

def returntime():
    return time.strftime("%H:%M:%S")

yrnum = time.strftime("%Y")
mnthnum = time.strftime("%b")
dayzum = time.strftime("%d")

signpath = ('/home/' + puser + '/signinlca')
yrpath = (signpath + '/' + yrnum)
mnthpath = (yrpath + '/' + mnthnum)
dayzpath = (mnthpath + '/' + dayzum)


# In[84]:

if os.path.isdir(signpath) == True:
    print 'Path is there'
else:
    print 'Path not there'
    os.mkdir(signpath)


# In[85]:

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


# In[73]:

firnam = raw_input('first name: ')
lasnam = raw_input('last name: ')
tshir = raw_input('tshirt size: ')
cofvol = raw_input('coffee volc: ')
comen = raw_input('comments: ')
betdict = dict()
betdict.update({'first-name' : firnam})
betdict.update({'last-name' : lasnam})
betdict.update({'signin-date' : returndate()})
betdict.update({'signin-hrmin' : returntime()})
betdict.update({'tshirt-size' : tshir})
betdict.update({'coffees' : int(cofvol)})
betdict.update({'comments:' : comen})
convj = json.dumps(betdict)
puser = getpass.getuser()
os.chdir(dayzpath)
opday = open((firnam + lasnam) + '.json', 'w')
opday.write(str(convj))
opday.close()


# In[93]:

signoutz = open((firnam + lasnam) + '.json', 'w')

comout = raw_input('out comments: ')
outdic = dict()
outdic.update({'signout-date': returndate})
outdic.update({'signout-time': returntime})
outdic.update({'signout-comment': comout})


# Current path is wcmckee@localhost:~/signinlca/18/Jan/2015$
# This is backwards and should be ~/signinlca/2015/Jan/18.
# 
# make path /home/user/signinlca/2015 (year)
# 
# make path /home/user/signinlca/Jan (month)
# 
# make path /home/user/signinlca/18 (day)

# In[80]:

time.strftime("%Y") #This is the year

time.strftime("%d") #This is the day

time.strftime("%b") #This is the month


# In[92]:

signoutz = open((firnam + lasnam) + '.json', 'w')

comout = raw_input('out comments: ')
outdic = dict()


# In[90]:

outdic.update({'signout-date': returndate})
outdic.update({'signout-time': returntime})


# In[ ]:




# In[ ]:



