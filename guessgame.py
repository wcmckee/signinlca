import random
#What numbers do you  want to guess. Guess between 0,10,
#20,30 30,40 etc

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

     innumz = ('Enter a number between ' + str(farchez) + ' and ' + str(lownumz))  

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
    
