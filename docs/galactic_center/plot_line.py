"""Plot count spectrum of Galactic center events around 130 GeV line feature.

This script generates a plot comparable to Figure 11 in this paper:
http://adsabs.harvard.edu/abs/2013arXiv1305.5597F 

Christoph Deil, 2013-09-12
"""
import pyfits
import matplotlib.pyplot as plt

events = pyfits.getdata('line_gtmktime.fits')
energy = events.data['ENERGY']
print('Number of events: ', len(energy))

plt.hist(energy)
plt.savefig('line_spectrum.png')
