import random
import urwid
#What numbers do you  want to guess. Guess between 0,10,
#20,30 30,40 etc

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


palette = [
     ('banner', 'dark red', 'dark blue'),
     ('streak', 'dark red', 'dark blue'),
     ('bg', 'dark red', 'dark blue'),]

numchez = 0

for guesz in range(10):
     #print (numchez + 10)
     farchez = (numchez)
     numchez = (numchez + 10)


     def GetNum():
          return random.randint(farchez,numchez)


     randnum = GetNum()
     #randnum = random.randint(0,9)
     #numtak = numchez - 10
     lownumz = (numchez)

     innumz = ('Enter a number between ' + str(farchez) + ' and ' + str(lownumz) + ': ')  

#def GiveNum():
#     return raw_input(innumz)

#GiveNum() = guesnum
     guesnum = raw_input(innumz)
     guesintz = int(guesnum)
     print guesintz
     print randnum
     if guesintz == randnum:
          txt = urwid.Text('You Win!')
          map1 = urwid.AttrMap(txt, 'streak')
          fill = urwid.Filler(map1)
          map2 = urwid.AttrMap(fill, 'bg')
          loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
          loop.run()
          print 'You Win!'
     else:
          print 'You Lose!'
    
