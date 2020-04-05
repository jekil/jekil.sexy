#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Publish settings.
SITEURL = "https://jekil.sexy"

# Disable debug options.
LOAD_CONTENT_CACHE = True
USE_LESS = False

# Third party services.
ADD_THIS_ID = 'ra-581885fa6aad787e'
#DISQUS_SITENAME = ''
GOOGLE_ANALYTICS = 'UA-2317228-19'
#GOOGLE_TAG_MANAGER = ''
#STATUSCAKE = { 'trackid': 'your-id', 'days': 7, 'design': 6, 'rumid': 1234 }
#PIWIK_URL = ""
#PIWIK_SITE_ID = 1