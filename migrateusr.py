
# coding: utf-8

# lookthisup
# copies user accounts and passwords to slave machines.

# In[1]:

import os
from datetime import datetime
#import gimpfu


# In[2]:

padir = ('/home/wcmckee/sellcoffee/pass/')


# In[3]:

lispad = os.listdir(padir)


# In[4]:

lispad


# In[5]:

os.chdir(padir)


# In[6]:

os.system('export UGIDLIMIT=500')


# In[10]:

os.system("awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534)' /etc/passwd > /home/wcmckee/sellcoffee/pass/passwd.mig")


# In[11]:

os.system("awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534)' /etc/group > /home/wcmckee/sellcoffee/pass/group.mig")


# In[12]:

os.system("awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534) {print $1}' /etc/passwd | tee - |egrep -f - /etc/shadow > /home/wcmckee/sellcoffee/pass/shadow.mi")


# In[13]:

os.system("cp /etc/gshadow /home/wcmckee/sellcoffee/pass/gshadow.mig")


# In[ ]:

#os.system("tar -zcvpf /home.tar.gz /home")


# In[ ]:

#tar -zcvpf ~/MOVE/mail.tar.gz /var/spool/mail

