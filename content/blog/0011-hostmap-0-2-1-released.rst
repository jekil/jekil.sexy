hostmap 0.2.1 released
######################
:date: 2009-12-26 21:46
:author: jekil
:category: Tools
:tags: discovery, dns enumeration, dns name, virtual host
:slug: hostmap-0-2-1-released
:status: published
:alias: /tools/hostmap-0-2-1-released/

| I am glad to release hostmap version 0.2.1.
| In this version there are a lot of bug fixes and some new features.

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

* Fixed handling of Errno::ECONNRESET in SSL certificate plugin.
* Upgraded net-dns to latest version from git repository.
* Fixed traceback on Mac OSX due to net-dns bug.
* Added check to enumerate host names with DNS TLD expansion.
* Added --print-maltego to get output in Maltego XML format.
* Fixed the exception handling architecture, now unknown exceptions
  that can be raised on not supported system are handled.
* Fixed traceback on FreeBSD due to raising of different exceptions.
* Added Metasploit auxiliary module in extra folder.
* Added validation of -t option, if it isn't an IP address hostmap is
  stopped.
* Added enumeration plugin timeout, by default at 10 minutes. Can be
  changed with user supplied --timeout option.
* Moved website from http://hostmap.sourceforge.net to
  http://hostmap.lonerunners.net
* Added warning message to fix traceback if missing libopenssl-ruby.

See the complete list of changes at http://hostmap.lonerunners.net/doc/Changelog.txt.

Download
--------

You can download it in the following formats:

* Source zip compressed, http://hostmap.lonerunners.net/downloads/hostmap-0.2.1.zip

Documentation
-------------

* hostmap user's manual: http://hostmap.lonerunners.net/doc/README.pdf
