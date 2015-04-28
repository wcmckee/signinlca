
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

# In[28]:

#from Crypto.PublicKey import RSA
import getpass
import os
import socket


# In[29]:

getusr = getpass.getuser()

oshsdir = ('/home/' + getusr + '/.ssh/')


# In[30]:

gethosz = socket.gethostname()


# In[31]:

#gethosz

#new_key = RSA.generate(2048, e=65537)
#privatekey = new_key.exportKey("PEM")
#publickey = new_key.publickey().exportKey("PEM")


# In[32]:

hoezapriv = (oshsdir + gethosz)

#hoezapriv.write(privatekey)

#hoezapriv.close()

#hoezapub = (oshsdir + gethosz + '.pub')

#hoezapub.write(publickey)

#hoezapub.close()


# In[33]:

#Need to move the public key to folder where webserver is running.
#Host machine then picks it up and writes to authorized keys.


# In[35]:

os.system('ssh-keygen -f ' + gethosz)


# In[26]:

bbautdir = ('/home/wcmckee/bbauthkeys/')


# In[27]:

os.system('cp ' + oshsdir + gethosz + '.pub /home/wcmckee/bbauthkeys/')


# In[ ]:



