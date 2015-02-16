
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
# Currently saves the file as firstname + lastname. 
# 
# How could this be improved? 
# 
# Signup/Signin System.
# 
# For signup - username, firstname, lastname, password(x2) is collected with input. Password is salted and hashed. 
# Username, firstname, lastname, and password (salt/hash) is added to a dict. Dict is converted to a json object.
# json object is saved as a json file in the folder signinlca / USERNAME-FOLDER / .signup.json
# 
# For signin. Username is collected with input. 
# Looks for folder of username. Opens .signup.json file - parsing data. 
# Save the value of 'password' as a varible.
# 
# Asks for password (getpass.getpass('Password please: ')
# salt/hash this password.
# save password attempt if error, otherwise true complete signin. 
# 
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

# In[52]:

import os
#import time
import json
import getpass
import arrow
import hashlib
from passlib.hash import pbkdf2_sha256
from walkdir import filtered_walk, dir_paths, all_paths, file_paths



# In[53]:

gmtz = arrow.utcnow()


# In[54]:

yrmt = gmtz.strftime("%Y")
mthza = gmtz.strftime("%m")
dthaq = gmtz.strftime("%d")
gmtz.strftime("%Y")
#yearz = strftime("%y", gmtime())
#monthz = strftime("%m", gmtime())
#dayz = strftime("%d", gmtime())


# In[55]:

yrmt


# In[56]:

mthza


# In[57]:

dthaq


# In[58]:

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


# In[59]:

if os.path.isdir(signpath) == True:
    print 'Path is there'
else:
    print 'Path not there'
    os.mkdir(signpath)


# In[60]:

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


# In[61]:

dayzpath


# In[62]:

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

# In[63]:

opsign = open('/home/wcmckee/signinlca/index.json', 'w')


# In[64]:

signup = raw_input('signup y/n ')
signupd = dict()

numchez = 0

if 'y' in signup:
    print('Welcome to signup!')
    firnam = raw_input('firstname: ')
    signupd.update({"firstname":firnam, })
    lasnam = raw_input('last name: ')
    
    usenam = raw_input('username: ')
    os.mkdir('/home/wcmckee/signinlca/usernames/' + usenam) 
    #passworz = passwd()
    
    pastest = getpass.getpass('password: ')

    pasnde = getpass.getpass('enter password again: ')
    
    signupd.update({"firstname":firnam, "lastname":lasnam,
                "username":usenam})
    
    hashez = pbkdf2_sha256.encrypt(pastest, rounds=200000, salt_size=16)
    signupd.update({"password":hashez})
    
    savjsn = open('/home/wcmckee/signinlca/usernames/' + usenam + '/.signups.json', 'a')
    jsncov = json.dumps(signupd)
    savjsn.write(jsncov)
    savjsn.close()
    print('Signup Complete. You can now signin with the username and password')

for logy in range(12):
    ferzr = (numchez)
    numchez = (numchez + 10)
    #usfaz = ('/home/wcmckee/signinlca/usernames/' + str(numchez) + usenam + '/index.json', 'w')
    os.mkdir('/home/wcmckee/signinlca/usernames/' + str(usenam) + '/' + str(logy))


# In[65]:

#hashez = pbkdf2_sha256.encrypt(pastest, rounds=200000, salt_size=16)
#signupd.update({"password":hashez})
#signin. need to open 
print ('signin!')
loginam = raw_input('Username: ')
#Open logins.json, find the username json object
loginpas = getpass.getpass('Password: ')
vercryp = pbkdf2_sha256.verify(loginpas, hashez)
if vercryp == True:
    print 'passwords correct - Logged in!'
    
else:
    print 'passwords wrong - Could not log!'
    #exit


# In[66]:

type(signupd)


# In[66]:




# In[67]:

#savjsn.write(jsncov)


# In[17]:

#savjsn.close()


# In[19]:

dicsigni = dict()


# In[21]:

signin = raw_input('signin? y/n')

if 'y' in signin:
    #uzname = raw_input('firstname: ')
    #lzname = raw_input('lastname: ')
    uzernam = raw_input('username: ')
    
    dicsigni.update({'username': uzernam})
    opsignin = open('/home/wcmckee/signinlca/usernames/' + str(uzernam) + ('/') + ('.signin.json'), 'w') 

    logtest = getpass.getpass('login password: ')
    loghash = pbkdf2_sha256.encrypt(logtest, rounds=200000, salt_size=16)
    vercryp = pbkdf2_sha256.verify(logtest, hashez)
    dicsigni.update({'password':loghash})
                    
    dicjsn = json.dumps(dicsigni)
    
    opsignin.write(dicjsn)
    opsignin.close()
    
                    
    #opsignin.write

    if pastest == True:
        print 'passwords correct'


# I have their signin data. Now what to do with it? Save it as a json object to be then used when they signin later? 
# 
# More security on it? Hash their usernames, firstnames, 2nd password?

# In[24]:

ersignin = open('/home/wcmckee/signinlca/usernames/' + str(uzernam) + ('/') + ('.signin.json'), 'r') 

paswz = ersignin.read()


# In[28]:

dicvert = json.loads(paswz)


# In[49]:

dicloin = dicvert['password']


# In[39]:

tresignin = open('/home/wcmckee/signinlca/usernames/' + str(uzernam) + ('/') + ('.signups.json'), 'r')



# In[40]:


convea =  tresignin.read()


# In[43]:

jsnver = json.loads(convea)


# In[47]:

jpas = jsnver['password']


# In[50]:

jpas


# In[51]:

dicloin


# In[118]:

loginz = raw_input('signin y/n ')
if 'y' in loginz:
    print('You signed in')
    #logoutz = None
else:
    logoutz = raw_input('signouts y/n ')


# In[119]:

if 'y' in loginz:
    firnam = raw_input('first name: ')
    lasnam = raw_input('last name: ')
    tshir = raw_input('tshirt size: ')
    cofvol = raw_input('coffee volc: ')
    comen = raw_input('comments: ')
    betdict = dict()
    betdict.update({'first-name' : firnam, 'last-name' : lasnam, 'signin-date' : returndate()})
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

files = file_paths(filtered_walk('/home/wcmckee/signinlca/', depth=100, included_files=['*.json']))


# In[483]:

for fie in files:
    #print fie
    print fie


# In[348]:




# In[ ]:



