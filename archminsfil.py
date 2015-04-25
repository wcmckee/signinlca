
# coding: utf-8

# This script moves the mins and hostname data to an archieve folder.
# fold struct is year/month/day/hour. new data created every 60 seconds. move html and json.

# In[63]:

import os
import arrow


# In[64]:

atimz = arrow.now()


# In[65]:

datim = atimz.datetime


# In[66]:

dayearz = atimz.year


# In[67]:

dayearz


# In[68]:

damonz = atimz.month


# In[69]:

dadayz = atimz.day


# In[70]:

dahorz = atimz.hour


# In[71]:

daminz = atimz.strftime('%M')


# In[72]:

daminz


# In[ ]:




# In[73]:

jsfilz = ('/home/wcmckee/sellcoffee/')


# In[74]:

arcpth = ('/home/wcmckee/sellcoffee/archive/')


# In[75]:

gtarzpth =  arcpth + '/' + str(dayearz)

gmonzpth = gtarzpth + '/' + str(damonz)

gdayzpth = gmonzpth + '/' + str(dadayz)

ghorzpth = gdayzpth + '/'  + str(dahorz)

gminzpth = ghorzpth + '/' + str(daminz)


# In[ ]:




# In[76]:

str(datim)


# In[77]:

if os.path.isdir(gtarzpth) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(gtarzpth)


# In[78]:

if os.path.isdir(gmonzpth) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(gmonzpth)


# In[79]:

if os.path.isdir(gdayzpth) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(gdayzpth)


# In[80]:

if os.path.isdir(ghorzpth) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(ghorzpth)


# In[81]:

if os.path.isdir(gminzpth) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(gminzpth)


# In[ ]:




# In[82]:

mnjsz = jsfilz + 'minutes.json'


# In[83]:

mnjsz


# In[84]:

comjsz = jsfilz + 'comps.json'


# In[85]:

indza = jsfilz + 'index.html'


# In[86]:

os.system('cp ' + mnjsz + ' ' + gminzpth + '/')

os.system('cp ' + comjsz + ' ' + gminzpth + '/')


# In[87]:

ghorzpth
os.system('cp ' + indza + ' ' + gminzpth + '/')


# In[88]:

rcentach = ('/home/wcmckee/sellcoffee/recentarchive/')


# In[89]:

os.system('cp ' + mnjsz + ' ' + rcentach)
os.system('cp ' + comjsz + ' ' + rcentach)
os.system('cp ' + indza + ' ' + rcentach)


# In[ ]:



