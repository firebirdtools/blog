#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ''

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""


# =============================================================================
# add m.css-theme
THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
                'static/m-dark.css']

M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['m.css/pelican-plugins']
PLUGINS = ['m.htmlsanity']



PLUGINS = ['m.htmlsanity', 'm.images']
M_IMAGES_REQUIRE_ALT_TEXT = False
STATIC_PATHS = ['static']



PLUGINS += ['m.htmlsanity', 'm.math']
M_MATH_RENDER_AS_CODE = False
M_MATH_CACHE_FILE = 'm.math.cache'



PLUGINS += ['m.htmlsanity', 'm.components']



SITEURL = 'https://firebirdtools.github.io/blog'