import pylab
import numpy as np

xmass = np.genfromtxt('upsilons-mass-pt-xaa.txt', delimiter=' ', dtype=None)
N = 330
min = 8.5
max = 11

pylab.hist(xmass, bins = N , range=[min, max])
pylab.xlabel('M (GeV/c^2)')
pylab.ylabel('Candidates /(MeV/c^2)')
pylab.show()
