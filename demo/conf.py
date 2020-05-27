import sys, os, subprocess

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer


project = u'Demo'
copyright = u'2015, My Name'
master_doc = 'index'
templates_path = ['_templates']
extensions = []
source_suffix = '.rst'
version = '2.3'
exclude_patterns = ['_build']

# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = False
html_sidebars = {
    '**': ['logo.html',
           'logo-text.html',
           'globaltoc.html',
           'localtoc.html',
           'searchbox.html']
}

html_logo = "steinwurf_logo_big.svg"

# ONLY for testing, this will make sure we use the guzzle_sphinx_theme in this
# repository
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import guzzle_sphinx_theme

extensions.append("guzzle_sphinx_theme")
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "http://my-site.com/docs/",
    "forkme_repository": {
        "provider": "GitHub",
        "url": "https://github.com/steinwurf/guzzle_sphinx_theme"
    }
}
