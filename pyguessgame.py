
# coding: utf-8

# In[65]:

import random
import urwid
import os
from pyfiglet import Figlet
import json
import random
import clint


# 

# Started as a simple python guessing game to be ran in terminal. 
# Asks for a number between 0-10 and works up to 100 - asking for the next 10 each time. 
# On win a urwid screen shows with 'You Win'. It would be nice if the whole game was inside of urwid.
# Figlet intergration. 

# In[39]:

f = Figlet()


# In[40]:

opusr = os.listdir('/home/wcmckee/signinlca/usernames/')


# In[40]:




# In[41]:

opusr


# In[42]:

ranumz = len(opusr)


# In[43]:

ranin = random.randint(0, ranumz)


# In[44]:

ranin


# In[45]:

opza =  opusr[ranin]


# In[46]:

opza


# In[47]:

lidte = open('/home/wcmckee/signinlca/usernames/' + opza + '/.signups.json', 'r')


# In[48]:

plid = lidte.read()


# In[51]:

tlid = json.loads(plid)


# In[64]:

firna = tlid['firstname']


# In[ ]:




# In[60]:

tlicha = tlid['lastname']


# In[66]:

fullna = firna + ' ' + tlicha


# In[67]:

from clint.textui import colored, puts

perf = puts(colored.yellow(fullna))

perf


# In[63]:

print f.renderText(opza)
print fullna


# In[ ]:




# In[38]:

def exitq(key):
    if key in ('enter', 'return'):
        raise urwid.ExitMainLoop()


# In[39]:

pallette = [
    ('banner', 'dark red', 'white'),
    ('streak', 'dark red', 'white'),
    ('bg', 'dark red', 'white'),]


# In[40]:

numchez = 0


# In[48]:

for guesz in range(10):
    farchez = (numchez)
    numchez = (numchez + 10)
    
    def GetNum():
        return random.randint(farchez,numchez)
    
    randnum = GetNum()
    
    lownumz = (numchez)
    
    innumz = ('Enter a number between ' + str(farchez) + ' and ' + str(lownumz) + ': ')
    
    guessnum = raw_input(innumz)
    
    guesintz = int(guessnum)
    
    print ('Guess was: ' + str(guesintz))
    #colomod
    print ('Correct was: ' + str(randnum))
    
    if guesintz == randnum:
        txt = urwid.Text(f.renderText( guessnum + ' ' + str(randnum) + ' You Win!'))
        numpor = urwid.Text(f.renderText(guessnum))
        map1 = urwid.AttrMap(txt, 'streak')
        mep = urwid.AttrMap(numpor, 'streak')
        fil = urwid.Filler(map1)
        fel = urwid.Filler(mep)
        map2 = urwid.AttrMap(fil, 'bg')
        loopa = urwid.AttrMap(fel, 'bg')
        looena = urwid.MainLoop(loopa, pallette, unhandled_input=exitq)
        looena.run()
        loop = urwid.MainLoop(fil, pallette, unhandled_input=exitq)
        loop.run()
        print f.renderText(guessnum + ' ' + str(randnum) + ' You Win!')
    else:
        txt = urwid.Text(f.renderText(guessnum + ' ' + str(randnum) + ' You Lose!'))
        map1 = urwid.AttrMap(txt, 'streak')
        fil = urwid.Filler(map1)
        map2 = urwid.AttrMap(fil, 'bg')
        loop = urwid.MainLoop(fil, pallette, unhandled_input=exitq)
        loop.run()
        print f.renderText(guessnum + ' ' + str(randnum) + ' You lose!')
        


# In[35]:

txt = urwid.Text(f.renderText(guessnum + ' ' + str(randnum)))
#numpor = urwid.Text(f.renderText(guessnum))
map1 = urwid.AttrMap(txt, 'streak')
#mep = urwid.AttrMap(numpor, 'streak')
fil = urwid.Filler(map1)
#fel = urwid.Filler(mep)
map2 = urwid.AttrMap(fil, 'bg')
#loopa = urwid.AttrMap(fel, 'bg')
#looena = urwid.MainLoop(loopa, pallette, unhandled_input=exitq)
#looena.run()
loop = urwid.MainLoop(fil, pallette, unhandled_input=exitq)
loop.run()


# In[ ]:

print 'The End'

