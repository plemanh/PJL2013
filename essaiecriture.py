#essai ecriture

import os
try:
    os.mkdir('/Users/Louis/Desktop/PJL2013/donnee/histart')
except OSError:
    pass

fich=open('/Users/Louis/Desktop/PJL2013/donnee/histart/histart.txt','w')

fich.write("this is a test")

fich.close()

