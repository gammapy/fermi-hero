.. _galactic_center_science_tool_images:

Create count and and model images with the Fermi Science Tools
==============================================================

Make a count image with ``gtbin``
---------------------------------

Run `gtbin <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/help/gtbin.txt>`_ to make a counts image:: 

   $ gtbin
   This is gtbin version ScienceTools-v9r31p1-fssc-20130410
   Type of output file (CCUBE|CMAP|LC|PHA1|PHA2|HEALPIX) [] CMAP 
   Event data file name[] gtmktime.fits
   Output file name[] count_image.fits
   Spacecraft data file name[] ../../spacecraft.fits 
   Size of the X axis in pixels[] 600
   Size of the Y axis in pixels[] 100
   Image scale (in degrees/pixel)[] 0.1
   Coordinate system (CEL - celestial, GAL -galactic) (CEL|GAL) [] GAL
   First coordinate of image center in degrees (RA or galactic l)[] 0
   Second coordinate of image center in degrees (DEC or galactic b)[] 0
   Rotation angle of image axis, in degrees[] 0
   Projection method e.g. AIT|ARC|CAR|GLS|MER|NCP|SIN|STG|TAN:[] CAR

Open up the image in `ds9 <https://hea-www.harvard.edu/RD/ds9/site/Home.html>`_
and use the following commands to get an image that looks like this:

* Select Scale -> Scale Parameters and ``sqrt`` with range 0 to 10.
* Color -> b

.. image:: galactic_plane_counts.png
   :scale: 70 %

Now use these options to get the following view of the same counts image:

* ``Analysis -> Smooth Parameters`` with a 3 pixel Gauss kernel
* Analysis -> Coordinate grid
* WCS -> Galactic and WCS -> Degrees 

.. image:: galactic_plane_counts_smoothed.png
   :scale: 70 %

Make a model image with ``gtbin``, ``gtexpcube2`` and ``gtmodel``
-----------------------------------------------------------------

Next we want to make a model image (a.k.a an "expected counts image") for the
diffuse Galactic and isotropic emission. See
`here <http://fermi.gsfc.nasa.gov/ssc/data/access/lat/BackgroundModels.html>`_
for information on these diffuse model components that are considered "background"
for gamma-ray source analysis. 

To get this image we need to run the following three Fermi ScienceTools in sequence:
* ``gtbin`` with the ``CCUBE`` option.
* ``gtexpcube2``
* ``gtmodel``

Compute an exposure cube
++++++++++++++++++++++++

`gtexpcube2 <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/help/gtexpcube2.txt>`_

Compute a diffuse model image
-----------------------------

`gtmodel <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/help/gtmodel.txt>`_

::

   ln -s $FERMI_DIR/refdata/fermi/galdiffuse/gal_2yearp7v6_v0.fits .
   ln -s $FERMI_DIR/refdata/fermi/galdiffuse/iso_p7v6source.txt .

