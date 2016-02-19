import pylab
import numpy as np

xmass = np.genfromtxt('upsilons-mass-xaa.txt', delimiter=' ', dtype=None)
N = 332
min = 8.5
max = 11

pylab.hist(xmass, bins = N , range=[min, max])
pylab.xlabel('M (GeV/c^2)')
pylab.ylabel('Candidates /(MeV/c^2)')
pylab.title('Candidates /(MeV/c^2) vs M (GeV/c^2)')
pylab.savefig('cern.png')
pylab.show()
