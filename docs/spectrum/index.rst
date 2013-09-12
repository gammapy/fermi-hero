.. _spectrum:

Spectrum
========

In this tutorial we will perform a full likelihood analysis of the AGN
PG1553+113. We will use the same dataset already used in the `official Fermi/LAT
collaboration likelihood tutorial
<http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/python_tutorial.html>`_
as well as in the `enrico tutorial
<http://enrico.readthedocs.org/en/latest/tutorial.html>`_, so that you can check
your results and have additional information by consulting the two other
webpages.

A note on directory structure
-----------------------------

In order to avoid confusions, it is always best to provide absolute paths for
all the files in the analysis. In this tutorial we will assume that you have
extracted the ``fermi-hero.tar.gz`` data tarball to the home directory of your
user (here, as an example, we use the username ``hero``), so that the directory
structure looks like this:

.. code-block:: bash
    
    $ cd /home/hero/fermi-hero
    $ ls
    excercises  solutions  spacecraft.fits
    $ ls excercises/spectrum/
    L120405112547B0489E7F68_PH00.fits

To start the tutorial, change directory to
``/home/hero/fermi-hero/excercises/spectrum``.


Make a config file
------------------

``enrico`` uses configuration files to run analysis (for a full description see
`the enrico documentation on the configuration files
<http://enrico.readthedocs.org/en/latest/configfile.html>`_).

You can use the `enrico_config` tool to quickly make a config file
called `pg1553.conf`. It will ask you for the required options
and copy the rest from a default config file `enrico/data/config/default.conf`:

.. code-block:: bash

   $ enrico_config pg1553.conf
   Please provide the following required options [default] :
   Output directory [~/fermi-hero/excercises/spectrum] :
   Target Name : PG1553+113
   Right Ascension: 238.92935
   Declination: 11.190102
   Options are : PowerLaw, PowerLaw2, LogParabola, PLExpCutoff
   Spectral Model [PowerLaw] : PowerLaw2
   ROI Size [15] : 15
   FT2 file [] : ~/fermi-hero/spacecraft.fits
   FT1 list of files [] : ~/fermi-hero/excercises/spectrum/L120405112547B0489E7F68_PH00.fits
   tag [LAT_Analysis] : spectrum
   Start time [239557418] : 239557417
   End time [334165418] : 256970880
   Emin [100] : 
   Emax [300000] : 

Note :

* Always give the full path for the files
* We used the PowerLaw2 model as in the Fermi tutorial.
* Time is give in MET
* Energy is given in MeV
* ROI size is given in degrees


Now you can edit this config file by hand to make further adjustments.

Make a model xml file
---------------------

The ST works using an sky model written in xml format. Often, this model is
complicated to generate. You can run enrico_xml to make such model of the sky
and store it into a xml file which will be used for the analysis.

.. code-block:: bash

   $ enrico_xml myanalysis.conf 
   use the default location of the catalog
   use the default catalog
   Use the catalog :  /CATALOG_PATH/gll_psc_v08.fit
   Add  24  source(s) in the ROI of  15.0  degrees
   3  source(s) have free parameters inside  3.0  degrees
   0  source(s) is (are) extended
   write the Xml file in /home/hero/fermi-hero/excercises/spectrum/PG1553+113_PowerLaw2_model.xml

.. note:: 
   Note that you give options for this step simply by mentioning
   the config file. For the `enrico_xml` tool, the relevant options
   are in the [space], [target] section.  The out file is given by [file]/xml.
