#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tony Locke'
SITENAME = 'Chellow'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('About', '/pages/about-chellow.html'),
    ('Archive', '/archives.html'),
    ('GitHub', 'https://github.com/WessexWater/chellow')
)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = "/home/tlocke/chellow-www/themes/simple"
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME = False
DISPLAY_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
DIRECT_TEMPLATES = (
    'index', 'tags', 'categories', 'archives', 'period_archives'
)

MENU_INTERNAL_PAGES = (
    #     ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
OUTPUT_PATH = 'docs'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
