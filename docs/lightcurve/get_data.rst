.. _getting_started_get_data:

Get Fermi LAT data
==================

For this tutorial, simply get TODO this tarball.
It contains all the data for all the exercises.

But you should still know how to get Fermi LAT data, so here's a short description.

Spacecraft file
---------------

The spacecraft file doesn't depend on the sky region or energy range you are interested in
... it is valid for the whole sky and all energies.

The only thing you have to watch out for is that your spacecraft file covers the time range
you want to analyse.
To obtain a spacecraft data file that covers the length of the Fermi mission (updated daily with new data) use 
these commands 

::

   wget ftp://legacy.gsfc.nasa.gov/FTP/fermi/data/lat/mission/spacecraft/lat_spacecraft_merged.fits
   mv lat_spacecraft_merged.fits spacecraft.fits


Photon files
------------

Usually you will do this via the
`FSSC data query web interface <http://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi>`_
as described in the
`Extract LAT Data analysis thread <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/extract_latdata.html>`_.

TODO: give screenshots and short description. 

Weekly files
------------

If you are a Fermi LAT power user (e.g. run analyses on several regions or
update your analyses every once in a while) or if there are several Fermi LAT data analysts
at your institute you should consider downloading the weekly photon and spacecraft files
as described `here <http://fermi.gsfc.nasa.gov/ssc/help/faq.html>`_::

   wget -m -P . -nH --cut-dirs=4 -np -e robots=off \
   ftp://legacy.gsfc.nasa.gov/fermi/data/lat/weekly/photon/
   wget -m -P . -nH --cut-dirs=4 -np -e robots=off \
   ftp://legacy.gsfc.nasa.gov/fermi/data/lat/weekly/spacecraft/

Note that the weekly photon files currently (2013, covering five years of Fermi observations)
are about 30 GB (giga-bytes) in size, so make sure you have the disk space and internet connection bandwidth.
