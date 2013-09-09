.. _getting_started_python:

Compute data summaries with ``Python``
======================================

In this section we will use the
`Python <http://www.python.org>`_ programming language interactive console and the
`PyFITS <https://pyfits.readthedocs.org/>`_ package and
`numpy <http://www.numpy.org>`_
(all come with the Fermi ScienceTools)
to compute data summaries of the various event files.

To start Python, simply type ``python`` on the command line.
This will show the Python prompt ``>>>`` where you can execute commands. 
To exit Python type ``CTRL + D``::

   $ python
   Python 2.7.2 (default, Apr 12 2013, 00:51:51) 
   [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 3 + 2
   5
   >>> ^D
   $

To check that you are actually using the Python in the Fermi ScienceTools::

   $ which python
   /Users/deil/software/fermi/ScienceTools-v9r31p1-fssc-20130410-x86_64-apple-darwin12.2.0/x86_64-apple-darwin12.2.0/bin/python

Remember that we had two photon files from the Fermi LAT data server and then ran
``gtselect`` to produce ``gtselect.fits`` and ``gtmktime`` to produce ``gtmktime.fits``::

   $ ftlist L1309081333300B976F4377_PH00.fits H
   
           Name               Type       Dimensions
           ----               ----       ----------
   HDU 1   Primary Array      Null Array                               
   HDU 2   EVENTS             BinTable    22 cols x 1065513 rows       
   HDU 3   GTI                BinTable     2 cols x 1790 rows          
   
   $ ftlist L1309081333300B976F4377_PH01.fits H
   
           Name               Type       Dimensions
           ----               ----       ----------
   HDU 1   Primary Array      Null Array                               
   HDU 2   EVENTS             BinTable    22 cols x 377253 rows        
   HDU 3   GTI                BinTable     2 cols x 1022 rows          
   
   $ ftlist gtselect.fits H
   
           Name               Type       Dimensions
           ----               ----       ----------
   HDU 1   Primary Array      Null Array                               
   HDU 2   EVENTS             BinTable    22 cols x 365387 rows        
   HDU 3   GTI                BinTable     2 cols x 2812 rows          
   
   $ ftlist gtmktime.fits H
   
           Name               Type       Dimensions
           ----               ----       ----------
   HDU 1   Primary Array      Null Array                               
   HDU 2   EVENTS             BinTable    22 cols x 312629 rows        
   HDU 3   GTI                BinTable     2 cols x 3419 rows          
 
Just to get used to Python and PyFITS, let's explore a bit what ``gtselect`` and ``gtmktime``
have done to the EVENTS and GTIs::

   $ python
   Python 2.7.2 (default, Apr 12 2013, 00:51:51) 
   [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 1790 + 1022
   2812
   >>> import pyfits
   >>> ph00 = pyfits.open('L1309081333300B976F4377_PH00.fits')
   >>> ph01 = pyfits.open('L1309081333300B976F4377_PH01.fits')
   >>> gtselect = pyfits.open('gtselect.fits')
   >>> gtmktime = pyfits.open('gtmktime.fits')
   >>> ph00.info()
   Filename: L1309081333300B976F4377_PH00.fits
   No.    Name         Type      Cards   Dimensions   Format
   0    PRIMARY     PrimaryHDU      31  ()            uint8
   1    EVENTS      BinTableHDU    169  1065513R x 22C  [E, E, E, E, E, E, E, E, E, D, J, J, I, 3I, J, I, D, E, E, E, E, E]
   2    GTI         BinTableHDU     46  1790R x 2C    [D, D]

TODO: finish this with some numpy calculations
