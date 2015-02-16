
# coding: utf-8

# In[1]:

import random
import urwid
import os
from pyfiglet import Figlet


# 

# Started as a simple python guessing game to be ran in terminal. 
# Asks for a number between 0-10 and works up to 100 - asking for the next 10 each time. 
# On win a urwid screen shows with 'You Win'. It would be nice if the whole game was inside of urwid.
# Figlet intergration. 

# In[21]:

f = Figlet()


# In[22]:

opusr = os.listdir('/home/wcmckee/signinlca/usernames/')


# In[23]:

import random


# In[24]:

opusr


# In[25]:

ranumz = len(opusr)


# In[26]:

ranin = random.randint(0, ranumz)


# In[27]:

ranin


# In[28]:

opza =  opusr[ranin]


# In[29]:

opza


# In[29]:




# In[30]:

ranumz


# In[31]:

print f.renderText(opza)


# In[38]:

def exitq(key):
    if key in ('enter', 'return'):
        raise urwid.ExitMainLoop()


# In[39]:

pallette = [
    ('banner', 'dark red', 'dark blue'),
    ('streak', 'dark red', 'dark blue'),
    ('bg', 'dark red', 'dark blue'),]


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



