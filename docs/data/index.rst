.. _data:

Data
====

.. warning:: Please **do not** download large files during the tutorial or the WIFI network will overload.
   We will distribute the software and data you need via USB sticks.

Download the `fermi-data.tar.gz` tarball from here (TODO),
then execute the following commands::

   tar zxvf fermi-data.tar.gz
   cd fermi-data
   $ du -hs *
   637M  excercises
   554M  solutions
   637M  spacecraft.fits

As you can see the `fermi-hero` folder contains a file ``spacecraft.fits`` as well as
two folders ``excercises`` and ``solutions``:

* `excercises` contains the input data files you'll need for the excercises.
  This is where you can run the analyses yourself by following the instructions given in the
  various tutorial sections.
* `solutions` contains all files after you've run the commands.
  You can use it as a reference or to skip very time-consuming steps by just copying over the
  relevant file from `solutions` to `excercises`     

TODO: give overview table of data sets used in this tutorial.

::

   $ ls -1 exercises
   getting_started
   image
   lightcurve
   spectrum
