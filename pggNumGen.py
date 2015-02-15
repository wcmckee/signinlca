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

savlis = open('/home/wcmckee/pgg/data.json', 'a')      
savlis.write(str(ranumlis))
savlis.close()
