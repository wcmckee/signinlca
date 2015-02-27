
# coding: utf-8

# <h1>LockAcc</h1>
# 
# Lock Account User Management System
# 
# Script to delete, create, lock, and change passwords for users. 
# 
# Script runs and gives choice for input. a b c d e etc...
# 
# 
# 
# Script to lock username. Asks for what user you want to lock, delete, create, lock or change password. 
# 

# In[2]:

import os
import getpass


# In[ ]:

#Menu that displays all the options. 
#eg 1 to delete user
#2 to create user
#3 to lock user
#4 to change password
print('a to delete a user, b to create a user, c to lock a user, and d to change password') 
selectchoic = raw_input('Select task by letter: ')

#selectchoic = int(selectchoic)
if str('c') in selectchoic:
#lockusr = raw_input('Do you want to lock a user? y/n ')
#if 'y' in lockusr:
    locusa = raw_input("User to lock: ")
    os.system('sudo passwd -l ' + locusa) 
    os.system('sudo pgrep -u ' + locusa)
    os.system('sudo killall -KILL -u ' + locusa)


# In[ ]:

#deleusr = raw_input('Do you want to delete a user? y/n ')

#if 'y' in deleusr:
if str('a') in selectchoic:
    print 'y'
    locusa = raw_input("User to Delete: ")
    os.system('sudo passwd -l ' + locusa) 
    os.system('sudo pgrep -u ' + locusa)
    os.system('sudo killall -KILL -u ' + locusa)
    os.system('sudo userdel -r ' + locusa)
    


# In[ ]:

#makeusr = raw_input('Do you want to create a user? y/n ')

#if 'y' in makeusr:
if str('b') in selectchoic:
    print 'y'
    cruer = raw_input('Username to Create: ')
    crpas = getpass.getpass('Password for ' + cruer + ': ')
    usdir = ('sudo useradd -p ' + crpas + ' ' + cruer)
    os.system(usdir)
    chdirz = ('sudo passwd ' + chpasr + ' ' + chpasz)



# In[ ]:

#Change a password of a user
#Why not just edit the shadow file and paste encrupted
#password in there?

#chanpass = raw_input('Do you want to change a password? y/n ')

#if 'y' in chanpass:
if str('d') in selectchoic:
    print 'y'
    chpasr = raw_input('Username to change password: ')
    chpasz = getpass.getpass('Enter new password: ')
    chdirz = ('sudo passwd ' + chpasr + ' ' + chpasz)
    


# In[ ]:

#if str('t') in selectchoic:
    

