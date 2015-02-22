
# coding: utf-8

# In[75]:

from nose.tools import ok_, eq_
import random
import re
import nose.tools
#import signinlca
import time
import os


# In[ ]:




# In[ ]:

#nose.tools.assert_list_equal


# In[42]:

#Nose check dir is there
#Check username is in usernames folder
#Check user is in /home/


# In[57]:

#print len('erter23')


# In[66]:

#Need to nose test raw_input
#charinp = raw_input('Enter number')


# In[67]:

def testlenth():
    if len('blahesrs') > 7:
        assert True
    else:
        assert False

#def testchartyp():
    
# #   assert len('erter23') == 7


# In[73]:

import requests
import shutil


# In[71]:

def testdirmk():
    if os.path.isdir('/home/wcmckee/github') == True:
        assert True
    else:
        assert False
    #os.mkdir(gtsdrndir)
    
def testimgur():
    if 'http://i.imgur.com' in 'http://i.imgur.com/RfIHXaJ.jpg':
        #print rdz.url
        assert True
    else:
        assert False
        
#def testrequeget():
#    if requests.get('/home/wcmckee/github/signinlca/testroll.py', stream=True):
        
    
        #url = rdz.url
        #response = requests.get(url, stream=True)
        #with open(str(rdz.author) + '-reference.png', 'wb') as out_file:
        #    shutil.copyfileobj(response.raw, out_file)
        #    del response
        
#def test


# In[43]:

#def checkstrlen():
#    assert len( 'erter23') < 6
    


# In[45]:

#nose.core.logging.codecs


# In[46]:

#nose.run(


# In[47]:

#def testhomedir():
#    assert os.listdir('/home/wcmckee/') == True


# Test that the list is empty.

# In[49]:

#def teststr():
#    if ranumlis == []:
#        assert True
#    else:
#        assert False
        
#def testfullis():
#    if ranumlis == list:
#        assert True
#    else:
#        assert False
    
#def testrandnum():
#    if randmun == 5:
#        assert True
#    else:
#        assert False


# In[50]:

EMAIL_REGEXP = r'[\S.]+@[\S.]+'

def test_email_regexp():
#   # a regular e-mail address should match
   assert re.match(EMAIL_REGEXP, 'test@nowhere.com')

#   # no domain should fail
#    assert not re.match(EMAIL_REGEXP, 'test@')


# In[51]:

#import nose


# In[52]:

#nose.tools.assert_greater()

#nose.tools.


# In[54]:

#os.listdir('/home/wcmckee/signinlca/')
#os.system('ipython nbconvert /home/wcmckee/github/signinlca/testroll.ipynb --to python')



# In[10]:

#def testsum():
#    eq_(4+2,4)


# In[13]:

#get_ipython().magic(u'logstart')
#import random
#ranumlis = []
#ranlow = 0
#ranhigh = 9

#for ranez in range(10):
#      randmun = random.randint(ranlow, ranhigh)
#      ranumlis.append(randmun)

#      ranlow = (ranlow + 10)
#      ranhigh = (ranhigh + 10)

#print ranumlis


# In[ ]:

#def testlis():
    


# In[6]:

#def test():
#    assert False


# In[78]:

#def testpass():
#    pass

#Test counting 0,9 10,19 to 90,99.


# In[79]:

#def testcountonhundrd():
#    for coun in range(0,99):
#        yield coun


# In[ ]:

def testodd():
    for i in range(0,10):
        yield checkodd, i , i*2
        
def checkodd(n, nn):
    assert n % 3 == 0 or nn % 3 == 0
        


# In[77]:

#def testevens():
#    for i in range(0, 99):
#        yield checkeven, i, i*3
        
#def checkeven(n, nn):
#    assert n % 2 == 0 or nn % 2 == 0


# In[76]:

#Test 


# In[ ]:

#time.sleep(15)
#os.system('nosetests /home/wcmckee/github/signinlca/testroll.py')

