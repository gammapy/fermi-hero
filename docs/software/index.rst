.. _software:

Software
========

.. warning:: Please **do not** download large files during the tutorial or the WIFI network will overload.
   We will distribute the software and data you need via USB sticks.

To participate in the tutorial you should bring a Mac or Linux laptop.

This page describes how to install the software we need for the tutorial and how to check that it works properly.

If you have a Windows laptop, you can install `VirtualBox <https://www.virtualbox.org>`_
and then install Linux in a virtual machine. It's best to install a Linux distribution that is officially  
supported by the Fermi science tools (see `here <http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/>`_):
unfortunately the `Scientific Linux <https://www.scientificlinux.org>`_ distribution is very large (over 4 GB)
and `Ubuntu <http://www.ubuntu.com>`_ has known problems.
Therefore we recomment you try `Fedora <http://fedoraproject.org>`_, which should be similar enough to ScientificLinux for the
`Scientific Linux 6 64 bit libc 2.12 <http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/tar/ScienceTools-v9r31p1-fssc-20130410-x86_64-unknown-linux-gnu-libc2.12.tar.gz>`_
binary version of the ScienceTools to work.

**Check:** you should be able to open a terminal and do this::

   $ echo "Hello world"
   Hello world
   $

Overview
--------

You should install the following software:

* Fermi Science Tools
* FTOOLS = HEASOFT (includes fv)
* ds9
* TOPCAT
* Aladin (if you want)
* Enrico

Fermi Science Tools
-------------------

The main analysis software you will use for this tutorial is the Fermi data analysis software, called the
`Fermi science tools <http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/>`_.

The `Fermi Science Support Center <http://fermi.gsfc.nasa.gov/ssc/>`_ web pages contain a lot of information
about Fermi `data access <http://fermi.gsfc.nasa.gov/ssc/data/access/>`_ and
`data analysis <http://fermi.gsfc.nasa.gov/ssc/data/analysis/>`_.
If you have a problem you can't solve yourself (always try finding a solution yourself with Google first),
you can contact the official NASA `Fermi help desk <http://fermi.gsfc.nasa.gov/ssc/help/>`_ or post in
`this forum <https://groups.google.com/forum/#!forum/gammapy_enrico>`_. 

The most important piece of advice on the
`Installing the Fermi Science Tools <http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/>`_ page is:

> Downloading and installing the Fermi science tools from the binary tar files below is strongly recommended.
> The many minor variations in the various Unix systems makes building the tools from source challenging.

So download the binary tar file for your machine ... this will take a while because it's about 1 GB in size.
As an example, for Mac the file you get will be called ``ScienceTools-v9r31p1-fssc-20130410-x86_64-apple-darwin12.2.0.tar.gz``
or maybe if it is automatically unzipped after download it will be called ``ScienceTools-v9r31p1-fssc-20130410-x86_64-apple-darwin12.2.0.tar``.

After download you have to set up the Fermi science tools as described
`here <http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/README_BINARY_INSTALL_FERMI.txt>`_.

**Check:** you should be able to use the Fermi science tools from the Shell command line and via Python::

   $ which gtbin
   $ gtbin
   # abort with CTRL + C
   $ which python
   $ python
   >>> import UnbinnedLikelihood

FTOOLS = HEASOFT
----------------

`Fv: The Interactive FITS File Editor <http://heasarc.gsfc.nasa.gov/ftools/fv/>`_ is a flexible tool to view and edit
`FITS <http://fits.gsfc.nasa.gov>`_ files. Use `ds9` as an image viewer and `fv` to look at the content of Fermi event lists
(called `photon files <http://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/Cicerone_Data/LAT_Data_Columns.html#PhotonFile>`_).   

**Check:** Open up a Fermi event list as described `here <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/explore_latdata.html>`_.

* `FTOOLS --- A General Package of Software to Manipulate FITS Files <http://heasarc.nasa.gov/ftools/>`_
  E.g. the `ftlist command line tool <http://heasarc.gsfc.nasa.gov/ftools/caldb/help/ftlist.html>`_
  is very handy to check what is in a given FITS file.


ds9
---

`SAOImage DS9 <http://hea-www.harvard.edu/RD/ds9/site/Home.html>`_ is one of the best viewers for astronomical
2D images and 3D cubes ... please download it from `here <http://hea-www.harvard.edu/RD/ds9/site/Download.html>`_.

**Check:** Download and open up the following `FITS <http://fits.gsfc.nasa.gov>`_ files:

* Hubble space telescope image of the Antennae Galaxies
  (`FITS file <http://www.spacetelescope.org/static/projects/fits_liberator/datasets/antennae/blue.fits>`_ of the 2D image)
* Fermi LAT diffuse emission model (an outdated version, used here because of the small file size)
  (`FITS file <http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/aux/gll_iem_v02.fit>`_
  of the 3D cube with `log(energy)` on the third axis).

If you want:

* Some Hubble space telescope optical images `here <http://www.spacetelescope.org/projects/fits_liberator/datasets_archives/>`_.
* Some Chandra X-ray observatory X-ray images `here <http://chandra.harvard.edu/photo/openFITS/>`_

TOPCAT
------

`TOPCAT <http://www.star.bris.ac.uk/~mbt/topcat/>` is a Java program to view FITS tables.
Follow the installation instructions on the web. 

Aladin (optional)
-----------------

`Aladin --- A FITS image viewer (alternative to ds9) <http://aladin.u-strasbg.fr>`_
is a nice astronomical image and catalog viewer ... an alternative to ``ds9``.

Install it and give it a try if you want. 

Enrico
------

Producing a spectrum (global model and flux points in energy bins) or light curve (flux points in time bins)
requires calling a lot of Fermi science tools with the right parameters in the right order.

Luckily you have `Enrico  <http://enrico.readthedocs.org/en/latest/index.html>`_ to help you.
Enrico is a set of `Python <http://www.python.org>`_ scripts that take a single 
`config file <http://enrico.readthedocs.org/en/latest/configfile.html>`_ as input where you specify what
kind of analysis you want to run and the most important analysis parameters, and the run all Fermi science tools
in the right order (or in parallel where possible) with the right parameters for you.

Please install Enrico as described `here <http://enrico.readthedocs.org/en/latest/setup.html#install-enrico>`_.

**Check:** To check that Enrico is installed correctly run this command::

   $ enrico_setupcheck


Init file
---------

You should create a file `fermi-hero-init.sh` which sets up your shell for this tutorial.

Once all software is installed all you have to do is::

   $ source fermi-hero-init.sh

This is an example init file ... you'll have to adapt the PATHs / versions to your system::

   export FERMI_HERO = /Users/deil/FERMI_HERO
   
   export HEADAS=$FERMI_HERO
   source $HEADAS/headas-init.sh
   
   export FERMI_DIR=$FERMI_HERO/ScienceTools-v9r31p1-fssc-20130410-x86_64-apple-darwin12.2.0/x86_64-apple-darwin12.2.0
   source $FERMI_DIR/fermi-init.sh
   
   export ENRICO_DIR=$FERMI_HERO/enrico
   source $ENRICO_DIR/enrico-init.sh
   
   alias topcat="java -Xms512m -Xmx4024m -jar /Applications/TOPCAT.app/Contents/Resources/Java/topcat-full.jar"
   alias aladin="java -Xms512m -Xmx4024m -jar /Applications/Aladin.app/Contents/Resources/Java/Aladin.jar"
   
   # Add location of binaries to your PATH, e.g. for ds9:
   export PATH=$PATH:$FERMI_HERO


..

   Other
   -----
   
   By now you have all the software you need for the tutorial.
   
   If you would like to continue with gamma-ray data analysis, here are some tools you might find useful and can install if you like:
   
   * `wget <http://en.wikipedia.org/wiki/Wget>`_ to download files from the command line
   * Learning to use `scientific Python stack <http://www.scipy.org/about.html#core-packages>`_ and especially `IPython <http://ipython.org>`_ will make
     you highly productive at any data analysis task.
   * `Astropy --- A Community Python Library for Astronomy <http://www.astropy.org>`_
   * `APLpy (the Astronomical Plotting Library in Python) <http://aplpy.github.io>`_
