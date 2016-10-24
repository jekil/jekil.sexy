Ghiro Appliance Building
########################
:date: 2014-11-18 01:05
:author: jekil
:category: Tools
:tags: appliance, ghiro, image forensics
:slug: ghiro-appliance-building
:status: published
:alias: /tools/ghiro-appliance-building

All started with us thinking about a way to provide users with the
**simplest** and **fastest** method to test or deploy
`Ghiro <http://getghiro.org>`__, some users just want to give a try or
deploy their infrastructure with no pain in few minutes, and we like
challenges.

The game was achieving an plug and play "box" with:

-  Few requirements or no requirements.
-  The ability to use the appliance building technology in a continuous
   integration system to be used in developer's daily testing.

After evaluating some technologies, the winner was a conventional
"virtual appliance", because it requires only one **virtualization**
software (i.e. Virtualbox, Vmware). I love docker but it is more
demanding.

`Packer <http://packer.io>`__ was the framework used to create, starting
from configuration files and script, a brand new Ghiro Appliance running
the latest development release from
`GitHub <https://github.com/Ghirensics/ghiro>`__.

The appliance **building** script is open source and available under a
project dubbed
`ghiro-appliance <https://github.com/Ghirensics/ghiro-appliance>`__ on
Github.

To play with it you have two options:

#. Get the latest **stable** appliance, the appliance running the latest
   stable Ghiro, from `official Ghiro website <http://getghiro.org>`__.
#. Create your own **development** appliance, using the latest Ghiro
   development release

If you are a Ghiro hacker or you just want to live on the cutting edge
of image forensics, you are going for the second option for sure.

Creating a new Ghiro appliance from scratch is quite easy:

-  Download and install `Packer <http://packer.io>`__.
-  You must have VirtualBox installed and access to internet (to
   download Ubuntu's packages).
-  Check out
    `ghiro-appliance <https://github.com/Ghirensics/ghiro-appliance>`__ repository
   and run:

.. code-block:: console

    $ packer build template.json

You will see packer run an create the Ghiro appliance: spawn a
Virtualbox machine, run the initial setup, reboot, and install all
software required.

It can take more or less 30 minutes depending on your system
performance and internet speed.

Now you will get an .OVA file ready for use! For more documentation just
have a look
to `ghiro-appliance <https://github.com/Ghirensics/ghiro-appliance>`__ `README.md <https://github.com/Ghirensics/ghiro-appliance/blob/master/README.md>`__
and Ghiro's documentation.

 
