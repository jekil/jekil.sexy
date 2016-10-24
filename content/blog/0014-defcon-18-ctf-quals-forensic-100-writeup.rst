DEFCON 18 CTF quals - Forensic 100 writeup
##########################################
:date: 2010-06-19 15:51
:author: jekil
:category: Forensic
:tags: CTF, DEFCON, quals
:slug: defcon-18-ctf-quals-forensic-100-writeup
:status: published
:alias: /forensic/defcon-18-ctf-quals-forensic-100-writeup

Some times ago i get a lot of fun at **DEFCON 18 CTF qualifications**
with a group of really skilled friends. Now a bit later, here is my
writeup for some challenges.

First forensic challange of the DEFCON 18 CTF qualifications: the
suggestion was "*find the key*" and the related file is
`here <http://squidzrus.schleppingsquid.net/DC18-Qual-Walks/f100_6db079ca91c4860f.bin>`__.
(Mirrors:
`#1 <http://stalkr.net/files/defcon/2010/quals/forensics100/f100_6db079ca91c4860f.bin.gz>`__,
`#2 <http://n.pentest.jp/ctf2010/f100_6db079ca91c4860f.bin>`__)

.. code-block:: console

    $ file f100_6db079ca91c4860f.bin
    f100_6db079ca91c4860f.bin: x86 boot sector; partition 1: ID=0x7,
    starthead 0, startsector 31, 31558 sectors, extended partition table
    (last)11, code offset 0x0

Now take a look at the partition table.

.. code-block:: console

    $ xxd -l 512 f100_6db079ca91c4860f.bin
    0000000: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000010: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000030: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000040: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000050: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000060: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000070: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000080: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00000a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00000b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00000c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00000d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00000e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00000f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000100: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000110: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000120: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000130: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000140: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000150: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000160: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000170: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000180: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    0000190: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00001a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00001b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00001c0: 0101 0700 dffa 1f00 0000 467b 0000 0000  ..........F{....
    00001d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00001e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
    00001f0: 0000 0000 0000 0000 0000 0000 0000 55aa  ..............U.

    $ xxd -l 512 -s 15872 f100_6db079ca91c4860f.bin
    0003e00: eb52 904e 5446 5320 2020 2000 0208 0000  .R.NTFS    .....
    0003e10: 0000 0000 00f8 0000 3f00 ff00 1f00 0000  ........?.......
    0003e20: 0000 0000 8000 0000 457b 0000 0000 0000  ........E{......
    0003e30: 2205 0000 0000 0000 0200 0000 0000 0000  "...............
    0003e40: f600 0000 0100 0000 631f 85d4 4885 d422  ........c...H.."
    0003e50: 0000 0000 fa33 c08e d0bc 007c fb68 c007  .....3.....|.h..
    0003e60: 1f1e 6866 00cb 8816 0e00 6681 3e03 004e  ..hf......f.>..N
    0003e70: 5446 5375 15b4 41bb aa55 cd13 720c 81fb  TFSu..A..U..r...
    0003e80: 55aa 7506 f7c1 0100 7503 e9dd 001e 83ec  U.u.....u.......
    0003e90: 1868 1a00 b448 8a16 0e00 8bf4 161f cd13  .h...H..........
    0003ea0: 9f83 c418 9e58 1f72 e13b 060b 0075 dba3  .....X.r.;...u..
    0003eb0: 0f00 c12e 0f00 041e 5a33 dbb9 0020 2bc8  ........Z3... +.
    0003ec0: 66ff 0611 0003 160f 008e c2ff 0616 00e8  f...............
    0003ed0: 4b00 2bc8 77ef b800 bbcd 1a66 23c0 752d  K.+.w......f#.u-
    0003ee0: 6681 fb54 4350 4175 2481 f902 0172 1e16  f..TCPAu$....r..
    0003ef0: 6807 bb16 6870 0e16 6809 0066 5366 5366  h...hp..h..fSfSf
    0003f00: 5516 1616 68b8 0166 610e 07cd 1a33 c0bf  U...h..fa....3..
    0003f10: 2810 b9d8 0ffc f3aa e95f 0190 9066 601e  (........_...f`.
    0003f20: 0666 a111 0066 0306 1c00 1e66 6800 0000  .f...f.....fh...
    0003f30: 0066 5006 5368 0100 6810 00b4 428a 160e  .fP.Sh..h...B...
    0003f40: 0016 1f8b f4cd 1366 595b 5a66 5966 591f  .......fY\[ZfYfY.
    0003f50: 0f82 1600 66ff 0611 0003 160f 008e c2ff  ....f...........
    0003f60: 0e16 0075 bc07 1f66 61c3 a0f8 01e8 0900  ...u...fa.......
    0003f70: a0fb 01e8 0300 f4eb fdb4 018b f0ac 3c00  ..............<.
    0003f80: 7409 b40e bb07 00cd 10eb f2c3 0d0a 4120  t.............A
    0003f90: 6469 736b 2072 6561 6420 6572 726f 7220  disk read error
    0003fa0: 6f63 6375 7272 6564 000d 0a42 4f4f 544d  occurred...BOOTM
    0003fb0: 4752 2069 7320 6d69 7373 696e 6700 0d0a  GR is missing...
    0003fc0: 424f 4f54 4d47 5220 6973 2063 6f6d 7072  BOOTMGR is compr
    0003fd0: 6573 7365 6400 0d0a 5072 6573 7320 4374  essed...Press Ct
    0003fe0: 726c 2b41 6c74 2b44 656c 2074 6f20 7265  rl+Alt+Del to re
    0003ff0: 7374 6172 740d 0a00 8ca9 bed6 0000 55aa  start.........U.

Seems some sort of Windows image. Get a look at the full partition
table.

.. code-block:: console

    $ mmls f100_6db079ca91c4860f.bin
    DOS Partition Table
    Offset Sector: 0
    Units are in 512-byte sectors

    Slot    Start        End          Length       Description
    00:  Meta    0000000000   0000000000   0000000001   Primary Table
    (#0)
    01:  -----   0000000000   0000000030   0000000031   Unallocated
    02:  00:00   0000000031   0000031588   0000031558   NTFS (0x07)
    03:  -----   0000031589   0000031615   0000000027   Unallocated

Using these values we can extract the partitions with dd.

.. code-block:: console

    $ dd if=f100_6db079ca91c4860f.bin of=p0.bin bs=512 skip=0 count=1
    1+0 records in
    1+0 records out
    512 bytes (512 B) copied, 5.0705e-05 s, 10.1 MB/s
    $ dd if=f100_6db079ca91c4860f.bin of=p1.bin bs=512 skip=0 count=31
    31+0 records in
    31+0 records out
    15872 bytes (16 kB) copied, 0.000218534 s, 72.6 MB/s
    $ dd if=f100_6db079ca91c4860f.bin of=p2.bin bs=512 skip=31
    31585+0 records in
    31585+0 records out
    16171520 bytes (16 MB) copied, 0.298363 s, 54.2 MB/s
    $ dd if=f100_6db079ca91c4860f.bin of=p3.bin bs=512 skip=31589
    27+0 records in
    27+0 records out
    13824 bytes (14 kB) copied, 0.000205892 s, 67.1 MB/s

Now re-check partions with file.

.. code-block:: console

    $ file p\*.bin
    p0.bin: x86 boot sector; partition 1: ID=0x7, starthead 0,
    startsector 31, 31558 sectors, extended partition table (last)11,
    code offset 0x0
    p1.bin: x86 boot sector; partition 1: ID=0x7, starthead 0,
    startsector 31, 31558 sectors, extended partition table (last)11,
    code offset 0x0
    p2.bin: x86 boot sector, code offset 0x52, OEM-ID "NTFS    ",
    sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8,
    heads 255, hidden sectors 31, dos < 4.0 BootSector (0x0)
    p3.bin: data

Now take a quick look with strings at each partitions, if you are lucky
you can see the key. Anyway go ahead with the full analysis.

Now run foremost to carve files on all partitions.

.. code-block:: console

    $ foremost -i p0.bin -o p0
    Processing: p0.bin
    |*|
    $ foremost -i p1.bin -o p1
    Processing: p1.bin
    |*|
    $ foremost -i p2.bin -o p2
    Processing: p2.bin
    |*|
    $ foremost -i p3.bin -o p3
    Processing: p3.bin
    |*|

On p2.bin foremost recovers some file as we can see from audit.txt.

.. code-block:: console

    $ cat p2/audit.txt
    Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick
    Mikus
    Audit File

    Foremost started at Sun Jun 20 17:47:43 2010
    Invocation: foremost -i p2.bin -o p2
    Output directory: /home/jekil/Desktop/p2
    Configuration file: /etc/foremost.conf
    ------------------------------------------------------------------
    File: p2.bin
    Start: Sun Jun 20 17:47:43 2010
    Length: 15 MB (16171520 bytes)

    Num     Name (bs=512)           Size     File Offset     Comment

    0:    00000312.jpg           11 KB          159744
    1:    00000336.jpg            4 KB          172032
    2:    00000344.jpg            1 KB          176128
    3:    00001032.jpg           13 KB          528384
    4:    00001064.jpg           36 KB          544768
    5:    00001144.jpg           32 KB          585728
    6:    00001216.jpg            4 KB          622592
    7:    00000288.png            9 KB          147456       (634 x 278)
    Finish: Sun Jun 20 17:47:43 2010

    8 FILES EXTRACTED

    jpg:= 7
    png:= 1
    ------------------------------------------------------------------

    Foremost finished at Sun Jun 20 17:47:43 2010

Get a look at these images with a viewer, one image seems to contains a
kind of encoded (like base64) data but i haven't found an use of that,
another image contains some exif data, you can see that with exiftool or
a viewer with metadata support.

.. code-block:: text

    File size : 4378 bytes  
    File date : 2010:05:22 01:57:57
    Resolution : 116 x 102
    GPS Latitude : N 36d 8m 8.5s
    GPS Longitude: E 115d 9m 29s
    Comment : Who is the author?ASCII

Now it's time to get a look at the file system. Add every partition to
autopsy and search for interesting things.

In partition two we found a suspect file in C:\\key but it was deleted.

Anyway it's a NTFS partition so we can check $MFT for chunks of deleted
files. Examining that and searching for the key file we see an
interesting string encoded in Unicode (points are null byte)

.. code-block:: text

    n.o.t.d.e.l.e.t.e.d.,.n.e.v.e.r.existed

The key was "notdeleted,neverexisted".
