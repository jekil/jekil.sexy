hostmap 0.2.2 released
######################
:date: 2010-05-09 19:57
:author: admin
:category: Tools
:tags: discovery, dns enumeration, dns name, virtual host
:slug: hostmap-0-2-2-released
:status: published
:admin: /tools/hostmap-0-2-2-released

| I am glad to release hostmap version 0.2.2.
| In this version there are a lot of bug fixes and some new features.

Introduction
------------

hostmap is a free, automatic, hostnames and virtual hosts discovery tool
written in Ruby and licensed under GNU General Public License version 3
(GPLv3). It’s goal is to enumerate all hostnames and configured virtual
hosts on an IP address. The primary users of hostmap are professionals
performing vulnerability assessments and penetration tests.

Changes
-------

Some of the new features include:

* Fixed hostname dictionary "big" list name.
* Fixed DNS AXFR zone transfer check that was prone to false
  positives under some circumstances.
* Added automatic check for new updates. You can disable it in
  configuration file or using the option --without-update.
* Fixed DNS History plugin that can raise SystemExit under some
  strange circumstances.
* Changed the job scheduler. Now is more fast, robust and fine tuned.
* Added a dynamic thread pool, now you can use --threads to choose
  the number of concurrent threads.
* Some minor fixes.

See the complete list of changes at http://hostmap.lonerunners.net/doc/Changelog.txt.

Download
--------

You can download it in the following format:

* Source zip compressed, http://hostmap.lonerunners.net/downloads/hostmap-0.2.2.zip
* Github, https://github.com/jekil/hostmap

Documentation
-------------

* hostmap user’s manual: http://hostmap.lonerunners.net/doc/README.pdf
