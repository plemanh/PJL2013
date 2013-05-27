import pylab as pl
import numpy as np
t = np.linspace(0, 8 * np.pi, 100)
x = np.sin(t)
pl.plot(t, x)
pl.xlabel('Time')
pl.ylabel('Amplitude')
pl.ylim([-1.5, 1.5])
pl.show()

print "Test GIT"

