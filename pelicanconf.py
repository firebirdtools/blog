#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'firebird'
SITENAME = 'Blog'
SITEURL = ''

PATH = 'content'

# TIMEZONE = 'Europe/Paris'
TIMEZONE = 'Asia/Shanghai'	

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
#RELATIVE_URLS = True



# ============================================================================

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

PLUGINS += ['m.htmlsanity', 'm.code']




# =============================================================================
AUTHOR = 'firebird'
M_SITE_LOGO_TEXT = 'Blog'
SITENAME = 'Blog'

#PLUGINS = ['m.abbr',
#          'm.components',
#           'm.dox',
#           'm.dot',
#           'm.filesize',
#           'm.gl',
#           'm.gh',
#           'm.htmlsanity',
#           'm.images',
#           'm.link',
#           'm.math',
#           'm.metadata',
#           'm.plots',
#           'm.vk']



# =============================================================================
M_FAVICON = ('static/firebird.png', 'image/x-icon')
M_LINKS_NAVBAR1 = [('FBT', 'https://www.firebirdtool.com/', '', []),                   
                   ('Docs', 'https://www.firebirdtool.com/doc-cpplogging/', '', [
                        ])]


# =============================================================================

# 博客中第一个文件展开设置
M_COLLAPSE_FIRST_ARTICLE = True