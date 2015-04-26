
# coding: utf-8

# script that creates rsa key on new slave machine.
# 
# Hosts on webserver
# 
# client machine accesses webserver keys.
# copies to /home/ user /.ssh
# 
# writes .pub to authorized_keys
# 
# slave machine does rsync to client machine. 

# In[5]:

from Crypto.PublicKey import RSA
import getpass
import os
import socket


# In[8]:

getusr = getpass.getuser()

oshsdir = ('/home/' + getusr + '/.ssh/')


# In[6]:

gethosz = socket.gethostname()


# In[9]:

gethosz

new_key = RSA.generate(2048, e=65537)
privatekey = new_key.exportKey("PEM")
publickey = new_key.publickey().exportKey("PEM")


# In[11]:

hoezapriv = open(oshsdir + gethosz, 'w')

hoezapriv.write(privatekey)

hoezapriv.close()

hoezapub = open(oshsdir + gethosz + '.pub', 'w')

hoezapub.write(publickey)

hoezapub.close()


# In[ ]:

#Need to move the public key to folder where webserver is running.
#Host machine then picks it up and writes to authorized keys.


# In[12]:

bbautdir = ('/home/wcmckee/bbauthkeys/')


# In[13]:

os.system('cp ' + oshsdir + gethosz + '.pub /home/wcmckee/bbauthkeys/')


# In[ ]:



