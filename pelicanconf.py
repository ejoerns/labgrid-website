AUTHOR = 'labgrid'
SITENAME = 'labgrid'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = "labgrid-theme"

DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Download', 'pages/download.html'),
    ('Documentation', 'rauc.readthedocs.io'),
    ('Media', 'pages/media.html'),
    ('Blog', 'www.pengutronix.de/en/tags/rauc.html'),
    ('Support', 'pages/support.html'),
)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
