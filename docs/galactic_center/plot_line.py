"""Plot count spectrum of Galactic center events around 130 GeV line feature.

This script generates a plot comparable to Figure 11 in this paper:
http://adsabs.harvard.edu/abs/2013arXiv1305.5597F 

Christoph Deil, 2013-09-12
"""
import pyfits
import matplotlib.pyplot as plt

MEV_TO_GEV = 1e-3
E_MIN, E_MAX = 37.5, 222.5

events = pyfits.getdata('line_gtmktime.fits')
energy = MEV_TO_GEV * events.field('ENERGY')
selection = (energy > E_MIN) & (energy < E_MAX)
n_events = len(energy[selection]) 
print('Number of events: {0}'.format(n_events))

plt.figure(figsize=(8, 5))
plt.hist(energy, bins=37, range=(E_MIN, E_MAX))
plt.xlabel('Energy (GeV)')
plt.ylabel('Events / 5 GeV')
plt.xlim(E_MIN, E_MAX)
plt.savefig('gc_line_matplotlib.png')
