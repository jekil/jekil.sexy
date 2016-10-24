Running Ghiro appliance on ESXi
###############################
:date: 2014-06-16 23:48
:author: jekil
:category: Tools
:tags: ghiro
:slug: running-ghiro-appliance-on-esxi
:status: published
:alias: /tools/running-ghiro-appliance-on-esxi

`Ghiro <http://www.getghiro.org>`__ is a nice digital image forensics
tool (ok it is self promotion..) and it comes as appliance too, this is
great when you need a click and run environment to start processing
images ASAP.

The appliance is available in OVA format (for VirtualBox, VMware Player
and Workstation), unfortunatly the appliance generated with VirtualBox
defaults for Ghiro 0.1 can't run on VMware `vSphere
Hypervisor <http://www.vmware.com/products/vsphere-hypervisor/>`__
(former ESXi), so  starting from today it is available in OVF format for
Vmware ESXi.

If you need to run Ghiro on ESXi you can download the Ghiro appliance
for ESXi from `Ghiro official
website <http://www.getghiro.org/#download-section>`__, import it with
vSphere client and run it! It is tested on ESXi 5.5.x.

Have fun!
