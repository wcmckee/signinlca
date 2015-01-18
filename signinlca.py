
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

# In[1]:

import os
import time
import json
import getpass


# In[2]:

def returndate():
    return time.strftime(("%d" + "-" + "%b" + "-" + "%Y"))

def returntime():
    return time.strftime("%H:%M:%S")

puser = getpass.getuser()

yrnum = time.strftime("%Y")
mnthnum = time.strftime("%b")
dayzum = time.strftime("%d")

signpath = ('/home/' + puser + '/signinlca')
yrpath = (signpath + '/' + yrnum)
mnthpath = (yrpath + '/' + mnthnum)
dayzpath = (mnthpath + '/' + dayzum)


# In[3]:

if os.path.isdir(signpath) == True:
    print 'Path is there'
else:
    print 'Path not there'
    os.mkdir(signpath)


# In[4]:

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


# In[5]:

os.chdir(dayzpath)


# In[6]:

loginz = raw_input('signin y/n ')
logoutz = raw_input('signouts y/n ')


# In[7]:

if 'y' in loginz:
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
    opday = open((firnam + lasnam) + '.json', 'w')
    opday.write(str(convj))
    opday.close()
else:
    print ('not signing in')


# In[8]:

if 'y' in logoutz:
    comout = raw_input('out comments: ')
    outdic = dict()
    
    firnaz = raw_input('first name: ')
    lasnaz = raw_input('last name: ')
    outdic.update({'signout-date': returndate()})
    outdic.update({'signout-time': returntime()})
    outdic.update({'signout-comment': comout})
    conout = json.dumps(outdic)
    signoutz = open((firnaz + lasnaz) + '.json', 'a')
    signoutz.write(str(conout))
    signoutz.close()
else:
    print ('not signing out')


# In[ ]:



