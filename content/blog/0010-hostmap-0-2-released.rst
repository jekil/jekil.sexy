hostmap 0.2 released
####################
:date: 2009-12-17 13:11
:author: jekil
:category: Tools
:tags: hostmap, virtual host
:slug: hostmap-0-2-released
:status: published
:alias: /tools/hostmap-0-2-released

I am glad to release hostmap version 0.2.

Introduction
------------

hostmap is a free, automatic, hostnames and virtual hosts discovery tool
written in Ruby and licensed under GNU General Public License version 3
(GPLv3). It's goal is to enumerate all hostnames and configured virtual
hosts on an IP address. The primary users of hostmap are professionals
performing vulnerability assessments and penetration tests.

Changes
-------

Some of the new features include:

* Fully refactored and rewritten in Ruby.
* User requested interrupt (CTRL+C) now is handled.
* Added Rakefile to automatize task. For example readme and API
  documentation rebuilding.
* Changed info gathering plugin architecture. Now using PlugMan
  library.
* Added some host names to brute forcing dictionaries.
* Added parsing of alternate subject (subjectAltName) from X.509
  certificates.
* Added info gathering plugin using dnshistory.org.
* Added wildcard domains detection.
* Added wildcard X.509 certificate detection.
* Added -d option to use a user supplied list of DNS servers
* Added blacklist for second level TLD (for example co.uk) detection.
* Added an enumeration plugin to use Microsoft Bing via API. API key
  must be provided in configuration file.
* Added a configuration file (hostmap.conf) to keep user settings.
* Added option --http-ports to specify the ports to check for an
  HTTP/HTTPS service.

See the complete list of changes at
http://hostmap.sourceforge.net/doc/Changelog.txt.

Download
--------

You can download it in the following formats:

* Source gzip compressed, `https://sourceforge.net/projects/hostmap/files/hostmap/hostmap-0.2/hostmap-0.2.tar.gz/download <https://sourceforge.net/projects/hostmap/files/hostmap/hostmap-0.2/hostmap-0.2.zip/download>`__

* Source zip compressed, https://sourceforge.net/projects/hostmap/files/hostmap/hostmap-0.2/hostmap-0.2.zip/download

Documentation
-------------

hostmap user's manual: http://hostmap.sourceforge.net/doc/README.pdf
