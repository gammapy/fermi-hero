"""Compute correlated source excess and significance maps.

Christoph Deil, 2013-09-12
"""
import numpy as np
from numpy import sign, sqrt, log
from scipy.ndimage import convolve
import pyfits

def correlate_image(image, radius):
    """Correlate image with circular mask of a given radius.
    
    This is also called "tophat correlation" and it means that
    the value of a given pixel in the output image is the
    sum of all pixel values in the input image within a given circular radius.
    
    https://gammapy.readthedocs.org/en/latest/_generated/gammapy.image.utils.tophat_correlate.html
    """
    radius = int(radius)
    y, x = np.mgrid[-radius: radius + 1, -radius: radius + 1]
    structure = x ** 2 + y ** 2 <= radius ** 2
    return convolve(image, structure, mode='constant')

def significance_lima(n_observed, mu_background):
    """Compute Li & Ma significance.
    
    https://gammapy.readthedocs.org/en/latest/_generated/gammapy.stats.poisson.significance.html
    """
    term_a = sign(n_observed - mu_background) * sqrt(2)
    term_b = sqrt(n_observed * log(n_observed / mu_background) - n_observed + mu_background)
    return term_a * term_b


if __name__ == '__main__':
    counts = pyfits.getdata('counts.fits')
    model = pyfits.getdata('model.fits')

    radius = 5 # correlation circle radius
    correlated_counts = correlate_image(counts, radius)
    correlated_model = correlate_image(model, image)
    
    excess = correlated_counts - correlated_model
    significance = significance_lima(correlated_counts, correlated_model)
    
    header = pyfits.getheader('counts.fits')
    pyfits.writeto('excess.fits', excess, header, clobber=True)
    pyfits.writeto('significance.fits', significance, header, clobber=True)
