.. _getting_started_get_data:

Get Fermi LAT data
------------------

Spacecraft file
+++++++++++++++

The spacecraft file doesn't depend on the sky region or energy range you are interested in
... it is valid for the whole sky and all energies.

The only thing you have to watch out for is that your spacecraft file covers the time range
you want to analyse.
To obtain a spacecraft data file that covers the whole length of the Fermi
mission (updated daily with new data) use this command

::

   wget -O spacecraft.fits ftp://legacy.gsfc.nasa.gov/FTP/fermi/data/lat/mission/spacecraft/lat_spacecraft_merged.fits


Photon files
++++++++++++

Usually you will do this via the
`FSSC data query web interface <http://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi>`_
as described in the
`Extract LAT Data analysis thread <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/extract_latdata.html>`_.

TODO: give screenshots and short description. 


.. tip::
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


Getting data from the April 2011 Crab Nebula Flare
++++++++++++++++++++++++++++++++++++++++++++++++++

To carry out the aperture lightcurve excercise you will have to download the
photon data from the `FSSC data query web interface
<http://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi>`_. 
We are interested in photons from a region of 1 degree radius around the Crab
Nebula during the period of 16 days between April 8th and April 24th 2011. To
convert between calendar dates, MJD and Fermi MET (Mission Elapsed Time, or seconds
since January 1st, 2001), you can use the `NASA HEASARC xTime tool
<http://heasarc.gsfc.nasa.gov/cgi-bin/Tools/xTime/xTime.pl>`_.

Since we have already provided you with the whole-mission ``spacecraft.fits``
file, there is no need to download the spacecraft file for this period, so you
uncheck the ``Spacecraft data`` box.

The parameters for the photon query should therefore be:

.. table:: LAT query parameters

    ================================ =========================================
    Parameter                        Value
    ================================ =========================================
    Object Name                      Crab Nebula
    Equatorial coordinates (degrees) (83.6331,22.0145)
    Time range (MET)                 (323913600,325296000)
    Time range (Gregorian)           (2011-04-08 00:00:00,2011-04-24 00:00:00)
    Energy range (MeV)               (100,300000)
    Search radius (degrees)          1
    ================================ =========================================

After a brief wait, download the resulting photon file to the
``$FERMI_HERO/excercises/lightcurve`` directory and, optionally, rename it to
``photon.fits`` to make it easier to remember.
