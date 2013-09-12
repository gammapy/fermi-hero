.. _galactic_center_line:

The 130 GeV line
================

What is it?
-----------

TODO: write introduction

.. figure:: gc_line.png
   :scale: 90 %

   Galactic center 130 GeV line
   Reference: http://adsabs.harvard.edu/abs/2013arXiv1305.5597F

Event selection
---------------

As always we start by preparing the event list by running ``gtselect`` and ``gtmktime``.
Note that we can use the same photon files as input that we to make Galactic plane high-energy images,
because in both cases our event selection is a subset the event selection we specified when downloading the data.

TODO: describe rad, emin, emax values::

   $ gtselect infile=@events.txt outfile=line_gtselect.fits \
     ra=INDEF dec=INDEF rad=3 tmin=INDEF tmax=INDEF \
     emin=100 emax=1000000 zmax=100 evclass=2

   $ gtmktime scfile=../../spacecraft.fits evfile=line_gtselect.fits \
     filter="DATA_QUAL==1&&LAT_CONFIG==1&&ABS(ROCK_ANGLE)<52" \
     roicut=yes outfile=line_gtmktime.fits


Quick look with TOPCAT
----------------------

TODO: describe steps to create equivalent figure with TOPCAT


Nice plot with Python ``matplotlib``
------------------------------------

.. literalinclude:: plot_line.py
   :emphasize-lines: 2
   :linenos:

