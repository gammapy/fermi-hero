.. _getting_started:

Getting Started
===============

To get started, you will learn how to use some tools to download, prepare and explore Fermi LAT data.

Fermi LAT data consists of **event data files** and **spacecraft data files**.

.. note:: Throughout this tutorial we will use the terms **event** and **photon** interchangeably,
   because for the event classes we use the fraction of events that are not photons,
   but charged cosmic rays, is negligibly low (less than 1%).

   **Event file == Photon file == FT1 file**

   **Spacecraft file == FT2 file**


The spacecraft data file contains the information about the orbit position and pointing direction
as well as some status and quality information ... you can use the same spacecraft file (~700 MB for 5 years)
for all your analyses as long as it covers the time range you want to analyse.
That's all you need to know about the spacecraft data file ... simply give it's filename to the tools that require it to do their job.

The event data file contains a table of observed and reconstructed events.
where the most important event parameters are:

* **(RA, DEC)** (degrees). Equatorial coordinates ... called right ascension **RA** and declination **DEC**.
* **(L, B)** (degrees). Galactic coordinates ... called Galactic longitude **L** and latitude **B**.
* **ENERGY** (MeV)
* **TIME** (seconds). Mission elapsed time when the event was detected.
  (MET is the total number of seconds since 00:00:00 on January 1, 2001 UTC)

In this tutorial we will have a quick look at the Fermi LAT dataset by binning the events into histograms:

* A 2-dimensional **(L, B)** histogram is called a **counts image**.
* A 1-dimensional **ENERGY** histogram is called a **counts spectrum**.
* A 1-dimensional **TIME** histogram is called a **counts lightcurve**.

In the :ref:`spectrum`, :ref:`lightcurve` and :ref:`galactic_center` tutorials we will then show you how to create a
**flux spectrum**, **flux lightcurve** and **flux image**, where **flux = counts / exposure** and
**exposure = (effective area) x (observation time)** and in addition to exposure the spatial resolution, called point spread function (PSF),
and energy resolution have been taken into account.

If you are interested to at least get a basic understanding of the theory how Fermi LAT gamma-ray data analysis works,
have a look at the 
`Fermi LAT Instrument response functions <http://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/Cicerone_LAT_IRFs/>`_
and
`Fermi LAT Likelihood Analysis <http://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/Cicerone_Likelihood/>`_
section of the `Fermi LAT Manual, called Cicerone <http://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/>`_.
In this short Fermi-Hero tutorial we focus on **how to use the tools to obtain results**
instead of **what exactly the tools do and why (methods, theory)**.

Prerequisites
-------------

You should have installed and quickly tested the :ref:`software` and downloaded and extracted the Fermi-Hero tutorial :ref:`data`.

Steps
-----


.. toctree::
   :maxdepth: 1
   :numbered:

   first_look
   prepare_data
   python
   explore_events
   image_and_source_catalog
   summary
   

Additional reference
--------------------

For more details, see the following official Fermi LAT analysis threads:

* `Extract LAT Data <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/extract_latdata.html>`_
* `Data Preparation <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/data_preparation.html>`_
* `Explore LAT Data <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/explore_latdata.html>`_
* `Explore LAT Data (for Burst) <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/explore_latdata_burst.html>`_
