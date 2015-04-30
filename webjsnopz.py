
# coding: utf-8

# Website json opertaion.
# 
# opens up json data and saves index.html.

# In[23]:

import json
import os

import dominate
from dominate.tags import *

import arrow

import random


# In[24]:

lisimg = os.listdir('/home/wcmckee/sellcoffee/imgs/')


# In[ ]:




# In[25]:

ranlogo = random.choice(lisimg)


# In[26]:

ranlogo


# In[ ]:




# In[2]:

rdcompz = open('/home/wcmckee/sellcoffee/comps.json', 'r')

rdstrza = rdcompz.read()


# In[3]:

rdstrza


# In[4]:

strzadic = json.loads(rdstrza)


# In[5]:

strzadic


# In[ ]:




# In[6]:

minszlen = '/home/wcmckee/sellcoffee/mins/'

hoszlen = '/home/wcmckee/sellcoffee/hostnames/'


# In[7]:

hoslidz = os.listdir(hoszlen)


# In[8]:

#rdminza = open(minszlen + jsd, 'r')


# In[9]:

rdminz = open('/home/wcmckee/sellcoffee/minutes.json', 'r')

jsdaz = json.loads(rdminz.read())


# In[10]:

for hosld in hoslidz:
    print hosld
    rdhoz = open(hoszlen + hosld, 'r')
    rehoza = rdhoz.read()
    print rehoza
    rdhoz.close()


# In[11]:

#rdhoz = open(hoszlen + )


# In[12]:

#rdminz


# In[13]:

for jsd in jsdaz:
    print jsd
    rdminza = open(minszlen + jsd, 'r')
    rdreda = rdminza.read()
    print rdreda
    rdminza.close()


# In[14]:

gtim = arrow.now()


# In[15]:

import getpass


# In[16]:

gusr = getpass.getuser


# In[17]:

gusr()


# In[18]:

updatz = ('Updated by ' + gusr() + ' on ')


# In[19]:

str(gtim.datetime)


# In[20]:

updatz


# In[21]:

jsdaz


# In[27]:

ranlogo


# In[ ]:




# In[22]:

doc = dominate.document(title='BroBeur Minutes')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div().add(ol()):
        attr(cls='header')
        h1('BroBeur Minutes')
        p(img('imgs/' + ranlogo, src='imgs/' + ranlogo))
        h3(updatz)
        h4(str(gtim.datetime))
        #p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        #h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        #p(bodycom)
    
    

with doc:
    with div(id='usermins').add(ol()):
        for jsd in jsdaz:
            h4(jsd)
            rdminza = open(minszlen + jsd, 'r')
            rdreda = rdminza.read()
            p(rdreda)
            rdminza.close()
            #h1(rdz.title)
            #a(rdz.url)
            #p(img(rdz, src='%s' % rdz))
            #print rdz
            #p(img(rdz, src = rdz))
            #p(rdz)


                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))
    with div(id='hostuser').add(ol()):
        for hosld in hoslidz:
            h4(hosld)
            rdhoz = open(hoszlen + hosld, 'r')
            rehoza = rdhoz.read()
            p(rehoza)
            rdhoz.close()



#print doc


# In[83]:

print doc


# In[85]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/home/wcmckee/sellcoffee/index.html')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[ ]:




# In[ ]:



