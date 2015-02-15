
# coding: utf-8

# In[1]:

import random
import urwid


# In[3]:

def exitq(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


# In[5]:

pallette = [
    ('banner', 'dark red', 'dark blue'),
    ('streak', 'dark red', 'dark blue'),
    ('bg', 'dark red', 'dark blue'),]


# In[6]:

numchez = 0


# In[ ]:

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
        txt = urwid.Text('You Win!')
        map1 = urwid.AttrMap(txt, 'streak')
        fil = urwid.Filler(map1)
        map2 = urwid.AttrMap(fil, 'bg')
        loop = urwid.MainLoop(fil, pallette, unhandled_input=exitq)
        loop.run()
        print ('You Win!')
    else:
        print ('You Lose!')

