.. _galactic_center_maps:

Maps
====


Prepare the data
----------------

The following procedure is explained in :ref:`getting_started`.

You start by creating a file ``events.txt`` that contains the photon data files you downloaded.
Note that in this case there the Fermi LAT data server generated eight files, each only about 1 MB (mega-byte)
large because there are only few events above 10 GeV.::

   $ ls -1 *_PH??.fits > events.txt
   $ du -hs *_PH??.fits
   968K  L1309071835220B976F4330_PH00.fits
   1004K L1309071835220B976F4330_PH01.fits
   1.1M  L1309071835220B976F4330_PH02.fits
   1.2M  L1309071835220B976F4330_PH03.fits
   1.0M  L1309071835220B976F4330_PH04.fits
   1.1M  L1309071835220B976F4330_PH05.fits
   1.0M  L1309071835220B976F4330_PH06.fits
   840K  L1309071835220B976F4330_PH07.fits
   808K  L1309071835220B976F4330_PH08.fits
   
Now tun the following commands in sequence. ``gtselect`` will just take a few seconds,
``gtmktime`` a few minutes and ``gtltcube`` will take a few hours ... so we suggest
you copy the file ``gtltcube.fits`` from the solutions folder so that you can continue quickly ::


   $ gtselect infile=@events.txt outfile=gtselect.fits \
     ra=INDEF dec=INDEF rad=INDEF tmin=INDEF tmax=INDEF \
     emin=10000 emax=1000000 zmax=100 evclass=2

   $ gtmktime scfile=../../spacecraft.fits evfile=gtselect.fits \
     filter=DATA_QUAL==1&&LAT_CONFIG==1&&ABS(ROCK_ANGLE)<52 \
     roicut=yes outfile=gtmktime.fits

   $ gtltcube evfile=gtmktime.fits scfile=../../spacecraft.fits \
     outfile=gtltcube.fits dcostheta=0.025 binsz=1 

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

Compute an excess and significance image
----------------------------------------


TODO: Give a Python script to do it (tophat-correlate or PSF-correlate, then apply LiMa formula).

.. literalinclude:: make_source_images.py
   :emphasize-lines: 2
   :linenos:

