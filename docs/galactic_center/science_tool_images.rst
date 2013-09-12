.. _galactic_center_science_tool_images:

Create count, exposure and model images with the Fermi Science Tools
====================================================================

Make a count cube and image
---------------------------

Run `gtbin <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/help/gtbin.txt>`_ to make a counts image:: 

   $ gtbin
   This is gtbin version ScienceTools-v9r31p1-fssc-20130410
   Type of output file (CCUBE|CMAP|LC|PHA1|PHA2|HEALPIX) [] CMAP 
   Event data file name[] gtmktime.fits
   Output file name[] counts_image.fits
   Spacecraft data file name[] ../../spacecraft.fits 
   Size of the X axis in pixels[] 700
   Size of the Y axis in pixels[] 700
   Image scale (in degrees/pixel)[] 0.1
   Coordinate system (CEL - celestial, GAL -galactic) (CEL|GAL) [] GAL
   First coordinate of image center in degrees (RA or galactic l)[] 0
   Second coordinate of image center in degrees (DEC or galactic b)[] 0
   Rotation angle of image axis, in degrees[] 0
   Projection method e.g. AIT|ARC|CAR|GLS|MER|NCP|SIN|STG|TAN:[] TAN

Use `ds9 <https://hea-www.harvard.edu/RD/ds9/site/Home.html>`_ to look at it::

   $ ds9 -cmap b -scale sqrt counts_image.fits 


.. image:: ds9_gc.png
   :scale: 100 %




Compute an exposure cube
------------------------

`gtexpcube2 <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/help/gtexpcube2.txt>`_

Compute a diffuse model image
-----------------------------

`gtmodel <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/help/gtmodel.txt>`_

::

   ln -s $FERMI_DIR/refdata/fermi/galdiffuse/gal_2yearp7v6_v0.fits .
   ln -s $FERMI_DIR/refdata/fermi/galdiffuse/iso_p7v6source.txt .

