This OVF package requires unsupported hardware
##############################################
:date: 2015-03-15 13:47
:author: jekil
:category: Blog
:tags: sysadmin, virtualbox
:slug: this-ovf-package-requires-unsupported-hardware
:status: published
:alias: /blog/this-ovf-package-requires-unsupported-hardware/

I was trying to import a virtual image in **OVA** format inside a Vmware
**ESXi** (or
`vSphere Hypervisor <http://www.vmware.com/products/vsphere-hypervisor>`__
as it is dubbed today) when I stumbled in this error:

::

    This OVF package requires unsupported hardware.
    Details: Line 33: Unsupported hardware family 'virtualbox-2.2'.

As you che see in the following image:

|20130530152156|

This error is mentioning some kind of unsupported hardware by
vSphere hypervisor, what happened?

It usually occur when an OVA appliance exported by
`VirtualBox <https://www.virtualbox.org/>`__ is imported in vSphere, the
default hardware format used by VirtualBox doesn't fit the vSphere one,
so it is unable to understand how to import the machine.

To fix you should convert the OVA file in an **OVF** file compatible
with vSphere, thus this post could be titled "how to convert and OVA in
OVF" too.

First of all download the free converter: `Vmware OFT
Tool <http://communities.vmware.com/community/vmtn/server/vsphere/automationtools/ovf>`__.

Now you can convert the OVA in an OVF with the following command:

.. code-block:: console

    ovftool.exe --lax source.ova destination.ovf

This command will create three files: a .MF file, an .OVF file and a
.VMDK.

Open the .OVF file in a text editor and change all VirtualBox hardware.

Change this:

.. code-block:: xml

    <vssd:VirtualSystemType>virtualbox-2.2</vssd:VirtualSystemType>

with:

.. code-block:: xml

    <vssd:VirtualSystemType>vmx-07</vssd:VirtualSystemType>

Change this:

.. code-block:: xml

    <Item>
    <rasd:Address>0</rasd:Address>
    <rasd:Caption>sataController0</rasd:Caption>
    <rasd:Description>SATA Controller</rasd:Description>
    <rasd:ElementName>sataController0</rasd:ElementName>
    <rasd:InstanceID>5</rasd:InstanceID>
    <rasd:ResourceSubType>AHCI</rasd:ResourceSubType>
    <rasd:ResourceType>20</rasd:ResourceType>
    </Item>

with:

.. code-block:: xml

    <Item>
    <rasd:Address>0</rasd:Address>
    <rasd:Caption>SCSIController</rasd:Caption>
    <rasd:Description>SCSI Controller</rasd:Description>
    <rasd:ElementName>SCSIController</rasd:ElementName>
    <rasd:InstanceID>5</rasd:InstanceID>
    <rasd:ResourceSubType>lsilogic</rasd:ResourceSubType>
    <rasd:ResourceType>6</rasd:ResourceType>
    </Item>

Save and close. Now your edited file screwed the integrity check. To fix
it calculate the SHA1 for the .OVF file (for example using *sha1sum* or
*fciv.exe* (`download <http://support.microsoft.com/kb/841290>`__), open the .MF
file a substitute the present hash with the calculated one.

Now all should work.

.. |20130530152156| image:: {static}/images/2015/03/20130530152156.jpg
   :width: 300px
   :height: 155px
   :target: {static}/images/2015/03/20130530152156.jpg
   :class: img-center
