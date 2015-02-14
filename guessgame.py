import random
#What numbers do you  want to guess. Guess between 0,10,
#20,30 30,40 etc

numchez = 0

for guesz in range(10):
     print (numchez + 10)
     numchez = numchez + 10

     def GetNum():
          return random.randint(0,9)


     randnum = GetNum()
     #randnum = random.randint(0,9)


     innumz = ('Enter a number between 0 and 10: ')  

#def GiveNum():
#     return raw_input(innumz)

#GiveNum() = guesnum
     guesnum = raw_input(innumz)
     guesintz = int(guesnum)
     print guesintz
     print randnum
     if guesintz == randnum:
          print 'You Win!'
     else:
          print 'You Lose!'
    
