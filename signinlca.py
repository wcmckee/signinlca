
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
#import time
import json
import getpass
import arrow

import hashlib


# In[2]:

gmtz = arrow.utcnow()


# In[3]:

yrmt = gmtz.strftime("%Y")
mthza = gmtz.strftime("%m")
dthaq = gmtz.strftime("%d")
gmtz.strftime("%Y")
#yearz = strftime("%y", gmtime())
#monthz = strftime("%m", gmtime())
#dayz = strftime("%d", gmtime())


# In[4]:

yrmt


# In[5]:

mthza


# In[6]:

dthaq


# In[7]:

def returndate():
    return (dthaq + '-' + mthza + '-' + yrmt)

def returntime():
    return gmtz.strftime('%H:%M:%S')

puser = getpass.getuser()

yrnum = gmtz.strftime("%Y")
mnthnum = gmtz.strftime("%m")
dayzum = gmtz.strftime("%d")

signpath = ('/home/' + puser + '/signinlca')
yrpath = (signpath + '/' + yrnum)
mnthpath = (yrpath + '/' + mnthnum)
dayzpath = (mnthpath + '/' + dayzum)


# In[8]:

if os.path.isdir(signpath) == True:
    print 'Path is there'
else:
    print 'Path not there'
    os.mkdir(signpath)


# In[9]:

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


# In[10]:

dayzpath


# In[11]:

os.chdir(dayzpath)


# Make new account, use existing account. 
# 
# Database of existing accounts... static page of files.
# 
# Add password to account 
# 
# If you signin, doesn't ask if want to sign out.
# 
# If you signout, doesn't ask if you want to sign in.
# 
# Hash passwords

# When creating account asked for username (which could be firstname + lastname), and password. Passwords are hashed and when user tries to login the password inputed is compared to the hashed password. 
# 
# Save that hash as a varible that is then complared with the saved hash password.

# In[11]:




# In[12]:

from IPython.lib import passwd 


# In[13]:

signup = raw_input('signup y/n ')
if 'y' in signup:
    print('Welcome to signup!')


# In[14]:

if 'y' in signup:
    firnam = raw_input('firstname: ')
    lasnam = raw_input('last name: ')
    usenam = raw_input('username: ')
    passworz = passwd()


# In[15]:

decri = hashlib.sha512(firnam + lasnam)


# In[16]:

#decri.update('testing')


# In[16]:




# In[17]:

signin = raw_input('signin? y/n')

if 'y' in signin:
    uzname = raw_input('firstname: ')
    lzname = raw_input('lastname: ')
    uzernam = raw_input('username: ')
    passwaz = passwd()


# In[20]:

#passworz


# In[21]:

#passworz


# In[22]:

firnam


# In[23]:

uzname


# In[24]:

rers = hashlib.sha512(raw_input('testing: '))


# In[37]:

from passlib.hash import pbkdf2_sha256


# In[25]:

decri.hexdigest()


# In[26]:

terbo = hashlib.sha1(usenam)


# In[26]:




# In[27]:

usenam


# In[28]:

daetim = hashlib.sha1(rers.hexdigest())


# In[29]:

terbo.hexdigest()


# In[30]:

firnam


# In[31]:

pastest = getpass.getpass('password: ')


pasnde = getpass.getpass('enter password again: ')


# In[32]:

saltin = os.urandom(16)


# In[33]:

hpase = hashlib.md5()


# In[34]:

hpase.update(saltin + pastest)


# In[35]:

hpase.hexdigest()


# In[38]:

hashez = pbkdf2_sha256.encrypt(pastest, rounds=200000, salt_size=16)


# In[39]:

loginpas = getpass.getpass('Password: ')


# In[40]:

pbkdf2_sha256.verify(loginpas, hashez)


# In[ ]:




# In[492]:

if pastest == pasnde:
    print 'passwords correct'
    
else:
    print 'passwords wrong'


# In[488]:

print pastest


# In[471]:

faetim = hashlib.sha1(firnam)


# In[472]:

#daetim.hexdigest()


# In[473]:

#faetim.hexdigest()


# In[474]:

if daetim.hexdigest == terbo.hexdigest:
    print 'They are the same'
else:
    print 'they are not the same'


# In[475]:

#m.hexdigest()


# I have their signin data. Now what to do with it? Save it as a json object to be then used when they signin later? 
# 
# More security on it? Hash their usernames, firstnames, 2nd password?

# In[476]:

passworz


# In[478]:

loginz = raw_input('signin y/n ')
if 'y' in loginz:
    print('You signed in')
    #logoutz = None
else:
    logoutz = raw_input('signouts y/n ')


# In[479]:

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
    opday = open((dayzpath + '/' + firnam + lasnam) + '.json', 'w')
    opday.write(str(convj))
    opday.close()
else:
    print ('not signing in')


# In[480]:

if 'y' in logoutz:
    comout = raw_input('out comments: ')
    outdic = dict()
    
    firnaz = raw_input('first name: ' )
    lasnaz = raw_input('last name: ')
    outdic.update({'signout-date': returndate()})
    outdic.update({'signout-time': returntime()})
    outdic.update({'signout-comment': comout})
    conout = json.dumps(outdic)
    signoutz = open((dayzpath + '/' + firnaz + lasnaz) + '.json', 'a')
    signoutz.write(str(conout))
    signoutz.close()
else:
    print ('not signing out')


# In[481]:

os.listdir(dayzpath)


# In[481]:




# In[482]:

from walkdir import filtered_walk, dir_paths, all_paths, file_paths

files = file_paths(filtered_walk('/home/wcmckee/signinlca/', depth=100, included_files=['*.json']))


# In[483]:

for fie in files:
    #print fie
    print fie


# In[348]:




# In[ ]:



