.. _galactic_center_python_images:

Compute an excess and significance image with Python
====================================================

We would like to compute correlated ``excess = counts - background`` and significance
images of the sources detected by the Fermi LAT above 10 GeV in the inner part of the Galactic plane,
similar to the one we showed previously from the Fermi publication.

.. note:: What is statistical significance and how can I compute it?

   TODO 
   http://en.wikipedia.org/wiki/Statistical_significance

This functionality is not readily available as a command line
`Fermi Science Tool <http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/references.html>`_.

If would be possible to do it by using
`fgauss <http://heasarc.gsfc.nasa.gov/ftools/caldb/help/fgauss.txt>`_ and
`ftimgcalc <http://heasarc.gsfc.nasa.gov/ftools/caldb/help/ftimgcalc.html>`_.

Instead of using these command line `FTOOLs <http://heasarc.gsfc.nasa.gov/ftools/>`_ 
let's use a Python script ``make_source_images.py``: 

.. literalinclude:: make_source_images.py
   :emphasize-lines: 2
   :linenos:

TODO: explain script a bit.
