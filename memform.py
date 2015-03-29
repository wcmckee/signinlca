
# coding: utf-8

# Membership Form
# 
# Script to help fill out a form. 

# In[18]:

import json
import os
import getpass


# In[19]:

getusr = getpass.getuser()


# In[20]:

getusr


# In[ ]:

#Too many input. What about looping through a conf file 
#each line in conf file is new question. each line is 
#assigned var that is then turned into 
#KEY and VALUE user input.
#


# In[14]:

fordict = dict()


# In[ ]:

print ('Parent to complete this section: ')
firnam = raw_input('first name: ')
lasnam = raw_input('last name: ')
adrs = raw_input('street number and name: ')
adtow = raw_input('city/town: ')
fordict.update({'firstname': firnam, 'lastname': lasnam, 'street': adrs, 'city': adtow})

hnum = raw_input('home number: ')
mnum = raw_input('mobile number: ')

emad = raw_input('email address: ')

skol = raw_input('school: ')
fordict.update({'homenumber': hnum, 'mobilenumber': mnum, 'emailaddr': emad, 'school': skol})

yrlvl = raw_input('year of school (0 for left): ')

gndr = raw_input('gender: ')

ethnic = raw_input('ethnicity: ')

fordict.update({'year': yrlvl, 'gender': gndr, 'ethnic': ethnic})

npare = raw_input('Name of Parent: ')

empar = raw_input('Email address of Parent: ')

phpar = raw_input('Home number of Parent: ')

phwor = raw_input('Work number of Parent: ')

phmol = raw_input('Mobile number of Parent: ')

fordict.update({'nameparent': npare, 'emailparent': empar, 'homenumparent': phpar, 'worknumparent': phwor, 'mobilenumparent': phmol})


dietreq = raw_input('Any dietary requirments? ')

medcond = raw_input('Details of any medical conditions we should be aware of: ')

permis = raw_input('Do you give permission to enrol in YouthTek15, attend bus trip to Wellington and for photos to be used for reporting and promotional purposes ')

transpor = raw_input('I can provide safe transport to and from Te Takere each day ')

signam = raw_input('Signature: ')
fordict.update({'diet': dietreq, 'permission': permis, 'transport': transpor})


# In[9]:

fordict


# In[10]:

print ('Student to complete this sectionn: ')

whycom = raw_input('Why do you wish to participate in YouthTek15: ')


whatit = raw_input('What IT experience do you have: ')

whereyt = raw_input('Where did you hear able YouthTek15? ')

fordict.update({'why': whycom, 'what': whatit, 'where': whereyt})
undstan = raw_input('Bus Trip is only for those that attend full week: ')

partful = raw_input('I will actively participate in the project fully for the whole week.')


signatz = raw_input('Signature/username/screenname you want: ')

fordict.update({'bus': undstan, 'participate': partful, 'studsign': signatz})


# In[11]:

print ('School teacher to complete this section')

sccom = raw_input('Comments: ')

supportthis = raw_input('I fully support the application form: ')

signza = raw_input('Signature: ')

napost = raw_input('Name and Position: ')

fordict.update({'teacom': sccom, 'teasup': supportthis, 'teasig': signza, 'teanampos': napost})


# In[12]:

fordict


# In[16]:

convjson = json.dumps(fordict)


# In[17]:

convjson


# In[22]:

#Check to see if the username already there - if so error and ask for new username.


# In[25]:

if os.path.isdir('/home/' + getusr + '/membapp/') == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir('/home/' + getusr + '/membapp/')


# In[26]:

if os.path.isdir('/home/' + getusr + '/membapp/' + signatz) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir('/home/' + getusr + '/membapp/' + signatz)


# In[27]:

#save json file in /home/username/membapp/ usernames signatz.

fulurl = open('/home/' + getusr + '/membapp/' + signatz + '/app.json', 'w')


# In[28]:

fulurl.write(convjson)
fulurl.close()


# In[ ]:



