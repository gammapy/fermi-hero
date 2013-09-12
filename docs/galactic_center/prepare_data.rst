.. _galactic_center_prepare:

Prepare the data
================

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


   $ time gtselect infile=@events.txt outfile=gtselect.fits \
     ra=INDEF dec=INDEF rad=INDEF tmin=INDEF tmax=INDEF \
     emin=10e3 emax=316e3 zmax=100 evclass=2

   $ time gtmktime scfile=../../spacecraft.fits evfile=gtselect.fits \
     filter="DATA_QUAL==1&&LAT_CONFIG==1&&ABS(ROCK_ANGLE)<52" \
     roicut=yes outfile=gtmktime.fits

   $ time gtltcube evfile=gtmktime.fits scfile=../../spacecraft.fits \
     outfile=gtltcube.fits dcostheta=0.025 binsz=1 

On my laptop ``gtselect`` takes 2 seconds, ``gtmktime`` takes 4 minutes and ``gtltcube`` takes two hours!
