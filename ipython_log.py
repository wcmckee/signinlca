# IPython log file

#get_ipython().magic(u'logstart')
import random
import os
lies = open('/home/wcmckee/pgg/data.json', 'r')
#lies.read()
res = lies.read()
print res
for itez in res:
      print itez
lies.close()
