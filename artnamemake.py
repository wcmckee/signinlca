
# coding: utf-8

# art name make
# 
# script to make filenames that are then saved with the gimp image open.
# 
# Lookup 
# 
# pi computer setup:
# 
# naplesyellow - raspib+ with touchscreen monitor. wireless, keyboard attached, coboltblue mounted. 8gig sd card. Full. weezey debian
# 
# bloodred - raspi2b attached to hp monitor. Wacom Drawing tablet. No Keyboard. weezey debian
# 
# zincwhite - raspi2b. Headless. Ethernet. weezey debian.
# 
# bluecookies - dell xps laptop. 500gig of backups/music/movies. fedora21
# 
# limegreen - compaq laptop. backup /home/wcmckee fedora21 
# 
# localhost - hp chromebook. debian jessie. 
# 
# android - samsung android. 16gig sd card. 
# 
# rsync bloodred (192.168.1.8:/home) to  

# In[1]:

import os


# In[ ]:

os.system('rsync -azP 192.168.1.2:/home/wcmckee /home/wcmckee')


# In[4]:

os.system('rsync -azP /home/wcmckee wcmckee@192.168.1.2:/home/wcmckee')


# In[ ]:

os.system('rsync -azP 192.168.1.8:/home/wcmckee /home/wcmckee')


# In[ ]:

os.system('rsync -azP /home/wcmckee wcmckee@192.168.1.8:/home/wcmckee')

