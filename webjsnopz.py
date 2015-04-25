
# coding: utf-8

# Website json opertaion.
# 
# opens up json data and saves index.html.

# In[34]:

import json
import os

import dominate
from dominate.tags import *

import arrow


# In[2]:

rdcompz = open('/home/wcmckee/sellcoffee/comps.json', 'r')

rdstrza = rdcompz.read()


# In[3]:

rdstrza


# In[7]:

strzadic = json.loads(rdstrza)


# In[8]:

strzadic


# In[ ]:




# In[20]:

minszlen = '/home/wcmckee/sellcoffee/mins/'

hoszlen = '/home/wcmckee/sellcoffee/hostnames/'


# In[23]:

hoslidz = os.listdir(hoszlen)


# In[ ]:

#rdminza = open(minszlen + jsd, 'r')


# In[9]:

rdminz = open('/home/wcmckee/sellcoffee/minutes.json', 'r')

jsdaz = json.loads(rdminz.read())


# In[25]:

for hosld in hoslidz:
    print hosld
    rdhoz = open(hoszlen + hosld, 'r')
    rehoza = rdhoz.read()
    print rehoza
    rdhoz.close()


# In[ ]:

#rdhoz = open(hoszlen + )


# In[10]:

#rdminz


# In[15]:

for jsd in jsdaz:
    print jsd
    rdminza = open(minszlen + jsd, 'r')
    rdreda = rdminza.read()
    print rdreda
    rdminza.close()


# In[35]:

gtim = arrow.now()


# In[39]:

import getpass


# In[40]:

gusr = getpass.getuser


# In[42]:

gusr()


# In[54]:

updatz = ('Updated by ' + gusr() + ' on ')


# In[55]:

str(gtim.datetime)


# In[56]:

updatz


# In[57]:

jsdaz


# In[58]:

doc = dominate.document(title='BroBeur Minutes')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div().add(ol()):
        attr(cls='header')
        h1('BroBeur Minutes')
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


# In[59]:

print doc


# In[60]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/home/wcmckee/index.html')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[ ]:



