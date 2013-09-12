.. _virtual_box:

Virtual Box
===========

We have prepared a virtual box that contain all software and data you need for the tutorial.

We will pass around USB sticks that contain the 6.3 GB ``fermi-hero.ova`` virtual appliance
as well as `VirtualBox <https://www.virtualbox.org/>`_ installers for Mac and Windows.

.. warning:: Your machine should have have at least **10 GB of free disk space**
   and 6 GB or RAM. If you only have 4 GB of RAM you can try changing the VM RAM size
   to 3 GB or 2 GB in the VM settings, but then some or the ScienceTools might
   start to swap to disk and become really slow.


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

* Distributed as 6.3 GB file ``fermi-hero.ova`` in the `Open Virtualization Format <http://en.wikipedia.org/wiki/Open_Virtualization_Format>`_
* 20 GB disk (VM file size grows dynamically) in `VDI <http://en.wikipedia.org/wiki/VDI_(file_format)#Virtual_Disk_Image>`_ format
* 4 GB RAM
* 64-bit `Fedora <http://fedoraproject.org>`_ Linux Version 19 (specifically ``Fedora-Live-Desktop-x86_64-19-1.iso``)
* Do all analysis as user ``hero`` in the home directory ``/home/hero`` ... no login password set.
* If you need ``root`` access ... the password is ``root``. E.g. you can get a ``root`` terminal by typing ``su``
  and then install software using ```yum`` <http://yum.baseurl.org/wiki/YumCommands>`_. 

 