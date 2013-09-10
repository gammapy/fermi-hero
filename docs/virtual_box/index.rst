.. _virtual_box:

Virtual Box
===========

We have prepared a virtual box that contain all software and data you need for the tutorial.

Note that you should have at least **10 GB of free disk space**!

We will pass around USB sticks that contain the 6.3 GB ``fermi-hero.ova`` virtual appliance
as well as `VirtualBox <https://www.virtualbox.org/>`_ installers for Mac and Windows.

Installing the VirtualBox software
----------------------------------

First you have to install the `VirtualBox <https://www.virtualbox.org/>`_  software.

* If you have a Windows laptop, please double-click ``VirtualBox-4.2.18-88780-Win.exe``
  from the USB stick and click ``OK`` a few times to go through the installation process.
* For Mac, double-click ``VirtualBox-4.2.18-88780-OSX.dmg``.

For Linux we did not put VirtualBox binaries on the USB sticks because there are too
many Linux variants. Your best shot at installing VirtualBox on your Linux machine
is probably to use your system package manager.

* On ``Ubuntu`` or other Debian-based Linuxes:: 

   $ sudo apt-get install virtualbox 

* On ``Fedora``::

   $ sudo yum install virtualbox

You can also try and download a VirtualBox binary installer from https://www.virtualbox.org/.
In either case (package manager or binary installer) it's prabably a ~ 100 MB download,
so it'll take a while with our WIFI.

Installing the ``fermi-hero`` virtual appliance
-----------------------------------------------

To install the ``fermi-hero.ova`` vitual appliance into VirtualBox,
either open um VirtualBox and use ``File -> Import`` or double-click
the ``fermi-hero.ova`` file.

You can install the virtual box directly from the USB drive or by first
copying the ``fermi-hero.ova`` file to your hard drive. 

In any case this will create a virtual box called ``fermi-hero`` on your had disk
(a folder called ``fermi-hero`` with a large ``fermi-hero.vdi`` file,
a small ``fermi-hero.vbox`` file as well as some other stuff inside.
You'll never have to look at this folder, except if you are short on disk space check it's size.

.. note:: VMWare should also be capable of importing the ``fermi-hero.vdi`` appliance,
   so if you prefer VMWare (non-free, but a bit nicer in some ways) over VirtualBox (free),
   give it a try and let us know.

Starting and using the ``fermi-hero`` virtual machine
-----------------------------------------------------

To start the ``fermi-hero` virtual machine (VM), start VirtualBox (the window has
``Oracle VM VirtualBox Manager`` in the title) and double-click on the ``fermi-hero`` VM.

Fedora wil boot up and present you with a login screen for the user ``hero``.

Some information on the VM:

* 