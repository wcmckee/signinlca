
# coding: utf-8

# In[13]:

import os
import getpass
from passlib.hash import pbkdf2_sha256
import crypt, getpass, spwd
from Crypto.PublicKey import RSA


# In[14]:

fuliz = os.listdir('/home')


# In[15]:

fuliz


# In[16]:

#Chabge password for user
#pasuz = raw_input('User to change password: ')


# In[17]:

#logtest = getpass.getpass('new password: ')

#loghash = pbkdf2_sha256.encrypt(logtest, rounds=200000, salt_size=16)
#vercryp = pbkdf2_sha256.verify(logtest, hashez)


# In[18]:

#Enter user to delete.
#Even better, user to lock.

#delusa = raw_input('User to delete: ')
#locusa = raw_input('User to lock: ')
#os.system('sudo passwd -l ' + locusa) 


# In[19]:

#Read hashed passwords from /etc/shadow
#opshad = open('/etc/shadow', 'r')
#opshad.read()
#opshad.close()
#Better to do this with a python module. spwd reads
#shadow files done.
#Need to getpass and ask for password, comparing to 
#the password returned from spwd


# In[20]:

pan = raw_input("Enter Username to delete: ")


# In[21]:

#enc_pwd = spwd.getspnam(pan)[1]
#if enc_pwd in ["NP", "!", "", None]:
#    print "user '%s' has no password set" % pan
#if enc_pwd in ["LK", "*"]:
#    print "account is locked"
#if enc_pwd == "!!":
#    print "password has expired"


# In[22]:

gpas = getpass.getpass('Enter Username Password: ')


# In[32]:

encpass = spwd.getspnam(pan)[1]


# In[33]:

if crypt.crypt(gpas, encpass) == encpass:
    print ('True')
else:
    print "incorrect password"


# In[34]:

#print spwd.getspnam(pan)[1]


# In[35]:

#shpa = spwd.getspnam('wcmckee')[1]


# In[36]:

#spwd.getspall()


# In[37]:

#shpa


# rsa key generated for each user and stored in their
# /home/user/.ssh/ folder. Public key is emailed, added to test servers.

# In[38]:

new_key = RSA.generate(2048, e=65537)
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.exportKey("PEM")
print private_key 
sapriv = open('/home/wcmckee/.ssh/' + pan, 'w')
sapriv.write(private_key)
sapriv.close()

print public_key 
papriv = open('/home/wcmckee/.ssh/' + pan + '.pub', 'w')
papriv.write(public_key)
papriv.close()




# In[39]:

#Spin up digital ocean server, with public key and 
#user created.


# In[1]:

#import digitalocean


# In[2]:

#tok  = ('c54ea484dcf55053743215cdb37309cb77a153e9810f35851b4701d4c8bf2881')


# In[3]:

#digid = digitalocean.Manager(token='c54ea484dcf55053743215cdb37309cb77a153e9810f35851b4701d4c8bf2881')



# In[4]:

#digid.get_account


# In[15]:

#my_droplets = digid.get_all_droplets()


# In[16]:

#lisdrop = []


# In[17]:

#for myd in my_droplets:
#    print myd
    #lisdrop.append(myd.image)
    #
#    lisdrop.append(myd.ip_address)


# In[18]:

#lisdrop


# In[ ]:




# In[7]:

#droplet = digitalocean.Droplet(token=tok,
#                               name='Example',
#                               region='nyc2', # New York 2
##                               image= , # Ubuntu 14.04 x64
 #                              size_slug='512mb',  # 512MB
#                              backups=True)


# In[8]:

#droplet.create()


# In[9]:

#dimg = digid.get_all_images()


# In[10]:

#for di in dimg:
##    print di


# In[23]:

#opdel = os.listdir('/home/wcmckee/signinlca/deleteusers')


# In[24]:

#opdel


# In[ ]:

usrtodel = raw_input('Account to delete: ')


# In[ ]:

locacc = os.system('sudo passwd -l ' + usrtodel)


# In[ ]:

locacc


# In[ ]:

os.system('mv ' + '  ' + '/home/wcmckee/signinlca/usernames/' + usrtodel + ' /home/wcmckee/signinlca/username/deleteusers/')

