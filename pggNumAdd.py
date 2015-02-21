
# coding: utf-8

# In[23]:

# IPython log file

#get_ipython().magic(u'logstart')
import random
ranumlis = []
ranlow = 0
ranhigh = 9

for ranez in range(10):
      randmun = random.randint(ranlow, ranhigh)
      ranumlis.append(randmun)

      ranlow = (ranlow + 10)
      ranhigh = (ranhigh + 10)

print ranumlis

savlis = open('/home/wcmckee/pgg/roll.json', 'w')      
savlis.write(str(ranumlis))
savlis.close()


# Testing of playing pyguessgame. 
# Generates random numbers and plays a game.
# 
# Create two random lists of numbers 0/9,10/19,20/29 etc to 100.
# Compare the two lists. If win mark, if lose mark.
# 
# Debian

# In[24]:

#for ronum in ranumlis:
#    print ronum


# In[25]:

randict = dict()


# In[26]:

othgues = []
othlow = 0
othhigh = 9


# In[27]:

for ranez in range(10):
      randxz = random.randint(othlow, othhigh)
      othgues.append(randxz)

      othlow = (othlow + 10)
      othhigh = (othhigh + 10)

#print othgues


# In[28]:

tenlis = ['zero', 'ten', 'twenty', 'thirty', 'fourty',
          'fifty', 'sixty', 'seventy', 'eighty', 
          'ninety']


# In[29]:

#for telis in tenlis:
#    for diez in dieci:
#        print telis


# In[30]:

#randict


# Makes dict with keys pointing to the 10s numbers. 
# The value needs the list of random numbers updated.
# 
# Currently it just adds the number one.
# How to add the random number list?

# In[31]:

for ronum in ranumlis:
    #print ronum
    if ronum in othgues:
        print (str(ronum) + ' You Win!')
    else:
        print (str(ronum) + ' You Lose!')
    


# In[32]:

#dieci = dict()


# In[33]:

#for ranz in range(10):
    #print str(ranz) + str(1)#
#    dieci.update({str(ranz) + str(1): str(ranz)})
#    for numz in range(10):
        #print str(ranz) + str(numz)
#        print numz
#print zetoo


# In[34]:

#for diez in dieci:
#    print diez


# In[35]:

#for sinum  in ranumlis:
#    print str(sinum) + (str('\n'))
    #if str(sinum) in othhigh:
    #    print 'Win'
        


# In[36]:

#import os


# In[37]:

#os.system('sudo adduser joemanz --disabled-login --quiet -D')


# In[38]:

#uslis = os.listdir('/home/wcmckee/signinlca/usernames/')
#print ('User List: ')
#for usl in uslis:
#    print usl
#    os.system('sudo adduser ' + usl + ' ' + '--disabled-login --quiet')
    
#    os.system('sudo mv /home/wcmckee/signinlca/usernames/' + usl  + ' ' + '/home/' + usl + ' ')  


# In[39]:

#print dieci


# In[39]:




# In[ ]:



