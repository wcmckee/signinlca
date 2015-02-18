
# coding: utf-8

# In[1]:

import os
import getpass
from passlib.hash import pbkdf2_sha256
import crypt, getpass, spwd


# In[2]:

fuliz = os.listdir('/home')


# In[3]:

fuliz


# In[4]:

#Chabge password for user
#pasuz = raw_input('User to change password: ')


# In[5]:

#logtest = getpass.getpass('new password: ')

#loghash = pbkdf2_sha256.encrypt(logtest, rounds=200000, salt_size=16)
#vercryp = pbkdf2_sha256.verify(logtest, hashez)


# In[6]:

#Enter user to delete.
#Even better, user to lock.

#delusa = raw_input('User to delete: ')
#locusa = raw_input('User to lock: ')
#os.system('sudo passwd -l ' + locusa) 


# In[7]:

#Read hashed passwords from /etc/shadow
#opshad = open('/etc/shadow', 'r')
#opshad.read()
#opshad.close()
#Better to do this with a python module. spwd reads
#shadow files done.
#Need to getpass and ask for password, comparing to 
#the password returned from spwd


# In[8]:

pan = 'wcmckee'


# In[9]:

#enc_pwd = spwd.getspnam(pan)[1]
#if enc_pwd in ["NP", "!", "", None]:
#    print "user '%s' has no password set" % pan
#if enc_pwd in ["LK", "*"]:
#    print "account is locked"
#if enc_pwd == "!!":
#    print "password has expired"


# In[14]:

gpas = getpass.getpass('Enter Username Password: ')


# In[21]:

encpass = spwd.getspnam(pan)[1]


# In[20]:

if crypt.crypt(gpas, encpass) == encpass:
    print ('True')
else:
    print "incorrect password"


# In[10]:

print spwd.getspnam(pan)[1]


# In[11]:

#shpa = spwd.getspnam('wcmckee')[1]


# In[12]:

#spwd.getspall()


# In[13]:

#shpa


# In[13]:




# In[13]:




# In[ ]:



