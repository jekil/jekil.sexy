#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'Alessandro Tanasi'
SITENAME = u"jekil.sexy"
SUBTITLE = u"%s's thoughts" % AUTHOR
SITESUBTITLE = ''
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = '//en.gravatar.com/userimage/1102835/a961dde28318778e338efdf517ea68cb.png?size=120'
ROBOTS = 'index, follow'

# Paths.
PATH = 'content'
STATIC_PATHS = ['images', 'extra', 'public']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ['.git']

# Style.
THEME = "pelican-themes/flex"
BROWSER_COLOR = '#333'
PYGMENTS_STYLE = 'monokai'
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 100

# Locals.
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}
DEFAULT_PAGINATION = 5

# Debug (true in production).
LOAD_CONTENT_CACHE = False

# Blog conf.
MAIN_MENU = False
USE_FOLDER_AS_CATEGORY = False
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
DEFAULT_METADATA = {
    'status': 'draft',
}
COPYRIGHT_YEAR = date.today().year

# Feeds.
FEED_DOMAIN = 'http://feeds.feedburner.com'
FEED_ALL_ATOM = 'jekil_is_sexy?format=xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('envelope-o', '/pages/contact/'),
          ('linkedin', 'https://www.linkedin.com/in/alessandrotanasi'),
          ('github', 'https://github.com/jekil'),
          ('twitter', 'https://twitter.com/jekil'),
          ('rss', 'http://feeds.feedburner.com/jekil_is_sexy?format=xml'),
          )
TWITTER_USERNAME = 'jekil'
GITHUB_URL = 'https://github.com/jekil'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Plugins.
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'pelican_alias']
