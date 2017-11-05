[![Build Status](https://travis-ci.org/jekil/jekil.sexy.svg?branch=master)](https://travis-ci.org/jekil/jekil.sexy)
![](https://reposs.herokuapp.com/?path=jekil/jekil.sexy&color=brightgreen)
[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

Jekil.sexy
----------

This repository is the source code of [jekil.sexy](https://jekil.sexy), my personal blog.


Setup
=====

Requirements:

    apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev python-virtualenv pyhton-pip

Blog setup:

    pip install -r requirements.txt 

Deploy
======

To deploy new content:

* Create new content
* Commit & push (for the sake of vcs)
* LC_ALL=en_US.UTF-8 make rsync_upload

