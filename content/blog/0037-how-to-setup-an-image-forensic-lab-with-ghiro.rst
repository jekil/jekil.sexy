How to setup an Image Forensic lab with Ghiro
#############################################
:date: 2015-08-19 23:49
:author: jekil
:category: Tools
:tags: appliance, ghiro, image forensics
:slug: how-to-setup-an-image-forensic-lab-with-ghiro
:status: published
:alias: /tools/how-to-setup-an-image-forensic-lab-with-ghiro

This how to will guide you through the setup of an **Image Forensics**
lab, using `Ghiro <http://getghiro.org>`__, a free and open source image
forensics tool.

Ghiro comes also with a **virtual appliance** (it is a copy of Ubuntu
Linux with all you need already installed, you can run on your host) to
help people get a running Ghiro in few steps.

1. Ready for virtualization
---------------------------

You can run Ghiro Appliance in any host (Mac, Windows or Linux),  only a
virtualization software is requested. There are many out there, free and
commercial, for example
`Vmware <http://www.vmware.com/products/workstation>`__ or
`VirtualBox <https://www.virtualbox.org/>`__.

`VirtualBox <https://www.virtualbox.org/>`__ is a free and open source
virtualization software, so for the sake of this guide we are going to
use it, although you can use any other software to run Ghiro Appliance.

You need to have VirtualBox working, so download and install
`VirtualBox <https://www.virtualbox.org/>`__ following the instruction
on his website.

2. GET Ghiro Appliance
----------------------

Download Ghiro Appliance from `Ghiro
website <http://www.getghiro.org/#download>`__ in OVA format and
uncompress it, it is around 600Mb.

You will explode an .OVA file (the appliance), and a readme file with
setup instructions.

|Screen Shot 2015-08-19 at 01.38.55|

3. Import Appliance
-------------------

Now you can import the .OVA file inside VirtualBox. Open VirtualBox, go
in the menu File and click on "Import Appliance...", a screen like the
following will popup:

|Screen Shot 2015-08-19 at 01.44.05|

Select the .OVA file and than click "Continue":

|Screen Shot 2015-08-19 at 01.45.25|

Now a default setting page is proposed, just hit "Import":

|Screen Shot 2015-08-19 at 01.46.42|

After clicking "Import" the import process will start and in a couple of
minutes it will be ready:

|Screen Shot 2015-08-19 at 01.47.14|

When the appliance is imported you will see it in virtual machines list
(don't worry if you don't have all the machines listed in the
screenshots, I am sorry but I have many):

|Screen Shot 2015-08-19 at 01.49.26|

4. Network Configuration
------------------------

Most people fail configuring the network, so please pay attention.

Right click on your **Ghiro Appliance** on the Virtual Box Manager
window and click **Settings.**

|Screen Shot 2015-08-19 at 01.51.03|

Then choose the **Network ** tab.

|Screen Shot 2015-08-19 at 01.51.52|

You have to configure how the virtual machine can connect to your
network, so now you are asked to select the network interface you are
using and the type of link (bridged or host only).

In most cases you need to set "Attached to:" to "**Bridged Adapter**"
and you have to set the "Name" of the network card you are using your
for network, for example if you are using your wired interface named
"eth0", select "eth0" on the name drop down menu.

Remember to alway set "Attached to:" to "Bridged Adapter" or "Host-only
Adapter", never use NAT or any other option, it will not work due to how
networking is implemented in VirtualBox. For more information about
connectivity see the `VirtualBox
documentation <https://www.virtualbox.org/manual/UserManual.html>`__.

|Screen Shot 2015-08-19 at 01.51.52|

5. Start and Play
-----------------

Start the Ghiro Appliance selecting it and clicking on "Start". The boot
will start, when the appliance is ready you will see a screen like this
one.

|Screen Shot 2015-08-19 at 01.54.17|

The appliance IP address is printed on the screen, as highlighted:

|appliance_15|

What you Now just put that address in your browser and the Ghiro interface will
appear.

|Screen Shot 2015-08-19 at 23.42.56|

Now login in your browser with the same credentials and you will be ready to play

-  Login: **ghiro**
-  Password: **ghiromanager**

|Screen Shot 2015-08-19 at 23.44.30|

**Enjoy!** For any question Ghiro developer are available on the
`forum <https://forum.getghiro.org>`__ or `mailing
list <https://groups.google.com/d/forum/ghiro>`__.

.. |Screen Shot 2015-08-19 at 01.38.55| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.38.55.png
   :width: 246px
   :height: 126px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.38.55.png
.. |Screen Shot 2015-08-19 at 01.44.05| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.44.05.png
   :width: 882px
   :height: 750px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.44.05.png
.. |Screen Shot 2015-08-19 at 01.45.25| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.45.25.png
   :width: 882px
   :height: 750px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.45.25.png
.. |Screen Shot 2015-08-19 at 01.46.42| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.46.42.png
   :width: 882px
   :height: 750px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.46.42.png
.. |Screen Shot 2015-08-19 at 01.47.14| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.47.14.png
   :width: 882px
   :height: 750px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.47.14.png
.. |Screen Shot 2015-08-19 at 01.49.26| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.49.26.png
   :width: 882px
   :height: 750px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.49.26.png
.. |Screen Shot 2015-08-19 at 01.51.03| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.51.03.png
   :width: 854px
   :height: 722px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.51.03.png
.. |Screen Shot 2015-08-19 at 01.51.52| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.51.52.png
   :width: 854px
   :height: 722px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.51.52.png
.. |Screen Shot 2015-08-19 at 01.54.17| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.54.17.png
   :width: 724px
   :height: 607px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-01.54.17.png
.. |appliance_15| image:: {filename}/images/2015/08/appliance_15.png
   :width: 752px
   :height: 635px
   :target: {filename}/images/2015/08/appliance_15.png
.. |Screen Shot 2015-08-19 at 23.42.56| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-23.42.56.png
   :width: 660px
   :height: 431px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-23.42.56.png
.. |Screen Shot 2015-08-19 at 23.44.30| image:: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-23.44.30.png
   :width: 660px
   :height: 431px
   :target: {filename}/images/2015/08/Screen-Shot-2015-08-19-at-23.44.30.png
