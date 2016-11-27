A Raspberry Pi Home Dashboard
#############################
:date: 2016-11-27 17:39
:author: jekil
:category: Blog
:tags: raspberry
:slug: a-raspberry-pi-home-dashboard
:status: published

Some time ago I created an home dashboard, using a Raspberry Pi, to have all my favourite tools (i.e. Zabbix, Munin)
on a wall screen in my room.
Now I want to write down and share with everyone how I put it together.

The whole idea of this is to have the Raspberry Pi hidden behind the screen, so trailing Ethernet cables isn't ideal. Luckily the Pi supports a range of Wifi adapters, also latest Pi has integrated Wifi.

What you'll need
----------------

* Raspberry Pi (I used a spare old one)
* Micro SD Card (8 gigs is enough)
* HDMI cable
* Monitor/TV
* (Optional) Wifi Adapter
* (Optional) Monitor Mount


OS Setup
--------

Download the latest version of Raspian from `raspberrypi.org <https://www.raspberrypi.org/downloads/raspbian/>`_
and flash the microSD card with your program of choice. If you need help doing that check the `installation guide
<https://www.raspberrypi.org/documentation/installation/installing-images/README.md>`_.

Boot your Raspberry Pi from the flashed microSD card, login using the default credentials and run `raspi-config 
<https://www.raspberrypi.org/documentation/configuration/raspi-config.md>`_ with:

.. code-block:: console

    sudo raspi-config

You'll need to:

* Change the account/password from default.
* Enable SSH, to enable remote login.
* Expand the file system, so you can use all your microSD card space.
* Set the desktop environment to auto boot.
* Edit the internationalisation options.
* (Optional) Some monitor needs to enable overscan in order for the image to fill the screen.

If you want to be able to access your Pi from a static IP (very useful for reliable SSH access when it is tied up behind a flatscreen), you have two options to do this. You can either set a DHCP reservation on the router or modify the */etc/network/interfaces* file on the Pi itself.

In ther interfaces file, you'll need to make the changes to fit your network. for example:

.. code-block:: text

    auto eth0
    iface eth0 inet static
    address 192.168.1.69
    netmask 255.255.255.0
    network 192.168.0.0
    broadcast 192.168.1.255
    gateway 192.168.1.1

After a reboot you should be able to login via SSH.

OS Configuration
----------------

First of all, upgrade your system with:

.. code-block:: console

    sudo apt-get update && sudo apt-get upgrade -y

This will sync the time with Ubuntu's NTP server, it is a good idea to have it always in sync:

.. code-block:: console

    sudo apt-get install ntpdate
    sudo ntpdate -u ntp.ubuntu.com

X Setup
-------

Setup all X11 utilities and midori (a lightweight browser, you could also use epiphany, chromium or a host of other browsers):

.. code-block:: console

    sudo apt-get install -y lightdm unclutter lxde-core midori

Make sure the screen does not go to sleep, modify */etc/lightdm/lightdm.conf*. Add this line to the *[SeatDefaults]* section:

.. code-block:: text

    xserver-command=X -s 0 dpms

Edit */etc/xdg/lxsession/LXDE/autostart* and make sure the *@xscreensaver* line is commented out. In addition, we’ll be adding three options that prevent the screen from going blank:

.. code-block:: text

    # @xscreensaver -no-splash
    # Turn off screensaver
    @xset s off
    # Turn off power saving
    @xset -dpms
    # Disable screen blanking
    @xset s noblank
    # Hide the mouse cursor
    @unclutter

Create (or modify) *~/.config/lxsession/LXDE/autostart* and add the line:

.. code-block:: text

    @midori -e Fullscreen -a file:///home/pi/index.html

Create */home/pi/index.html* as a static HTML page with a little bit of Javascript to create the web slideshow effect, it will load all the web pages in the *urls* list after waiting for *setTimeout*:

.. code-block:: html

    <!doctype html>
    <html>
    <head>
    </head>
        <body>
            <iframe id="foo" style="position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;"></iframe>
    <script>
                (function() {
                    var e = document.getElementById('foo'),
                        f = function( el, url ) {
                            el.src = url;
                        },
                        // List here the URLs you want to show in your home dashboard.
                        urls = [
                        'http://www.cnn.com/',
                        'http://www.bbc.co.uk'
                        ],
                        i = 0,
                        l = urls.length;

                        (function rotation() {
                            if ( i != l-1 ) { 
                                i++
                            } else {
                                i = 0;
                            }
                            f( e, urls[i] );
                            setTimeout( arguments.callee, 90000 );
                        })();
                })();
            </script>
        </body>
    </html>

If you are going to show authenticated web pages, i.e. zabbix, you should authenticate yourself manually before.

Bonus
-----

If you want to turn off you dashboard for the night, you can simply add a *cronjob* service to shutdown the
Raspberry, running *sudo crontab -e* and adding:

.. code-block:: text

    0       0      *       *       1,2,3,4,5 /sbin/shutdown -h now

You could also want to setup VNC to remotely control your raspberry and run your maintenance without the need of
keyboard and mouse.

Enjoy
-----

As you have seen, getting metrics and dashboards is a relatively simple process and it is super easy to build your own, it is also cheap.

Here is the list of tutorials I used to bring my dashboard together:

* http://alexba.in/blog/2013/01/04/raspberrypi-quickstart/
* https://www.reddit.com/r/raspberry_pi/comments/50ujya/raspberry_pi_home_dashboard/
* https://gocardless.com/blog/raspberry-pi-metric-dashboards/
* https://gist.github.com/petehamilton/5705374
* https://gist.github.com/blackjid/dfde6bedef148253f987
* http://elinux.org/R-Pi_Troubleshooting
* https://weblogs.asp.net/bleroy/getting-your-raspberry-pi-to-output-the-right-resolution
* https://github.com/MobilityLab/TransitScreen/wiki/Raspberry-Pi
* http://blogs.wcode.org/2013/09/howto-boot-your-raspberry-pi-into-a-fullscreen-browser-kiosk
