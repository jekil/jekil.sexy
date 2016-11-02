Bringing up VirtualBox interface before starting Cuckoo
#######################################################
:date: 2014-08-27 18:43
:author: jekil
:category: Tools
:tags: cuckoo, virtualbox
:slug: bringing-up-virtualbox-interface-before-starting-cuckoo
:status: published
:alias: /tools/bringing-up-virtualbox-interface-before-starting-cuckoo/

I am getting older and I need to write down commands I use rarely.

`Cuckoo sandbox <http://www.cuckoosandbox.org/>`__ expects to found all
network interfaces configured in its configuration file up when you
start it.

If you configured Cuckoo to bind on, for example, VirtualBox virtual
interface although it is not up and working, Cuckoo will raise an error to
tell you it cannot operate with an interface down.

.. code-block:: text

    Cuckoo Sandbox 1.2-dev
    www.cuckoosandbox.org
    Copyright (c) 2010-2014

    2014-08-24 00:21:33,713 [root] CRITICAL: CuckooCriticalError: Unable to bind ResultServer on 192.168.56.1:2042: [Errno 99] Cannot assign requested address

The "Unable to bind ResultServer" error means that Cuckoo was unable to
bind the component used to fetch analysis' logs, it happens because your
virtual interface is down or missing.

To fix you have only to bring up your (virtual) interface. You should
create the virtual networking device and configure it.

With VirtualBox you have two ways to get a virtual interface up. The
quick and dirty one: just start and stop your virtual machine. The
cleanest, use the following commands to create the virtual network
interface and configure it:

.. code-block:: console

    # VBoxManage hostonlyif create
    # ip link set vboxnet0 up
    # ip addr add 192.168.56.1/24 dev vboxnet0

The first command tells VirtualBox to bring up an host-only vboxnet
interface, the rest is used to configure it.

Happy analysis!
