# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# -- Project information -----------------------------------------------------

project = 'Puttshack Cloud'
copyright = '2021, Shaloo Shalini'
author = 'Shaloo Shalini'

# The full version, including alpha/beta/rc tags
release = ''
source_suffix =  '.rst'

# -- General configuration ---------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Common Sphinx Extensions used to build html and pdf docs --------------

extensions = [
        'sphinx.ext.todo',
        'sphinx.ext.githubpages',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosectionlabel',
        'sphinx.ext.duration',
        'sphinx.ext.extlinks',
        'sphinx.ext.graphviz',
        'sphinx.ext.ifconfig',
        'sphinx.ext.intersphinx',
        'sphinxcontrib.contentui',
        'sphinxcontrib.spelling',
        'sphinxcontrib.openapi',
        'sphinxcontrib.redoc',
        'sphinxcontrib.swaggerui',
        'sphinx_git',
        'sphinx_panels',
        'sphinxcontrib.mermaid',
]

# -- Spelling Extension Configuration ----------------------------------------

spelling_lang='en_US'
spelling_show_suggestions=True
spelling_add_pypi_package_names = True
spelling_exclude_patterns=[]

# -- Redoc Extension configuration -------------------------------------------

redoc_uri = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'

def setup(app):
   app.add_css_file('theme_overrides.css')

# Commonly used filler content for PoC

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

inputs_required = '**Chris/Johnnie: Do you have any inputs for this section?**'

product_name = 'Puttshack Cloud APIs'

rst_epilog = """
.. |Lorem_ipsum| replace:: %(lorem_ipsum)s
.. |inputs_required| replace:: %(inputs_required)s
.. |product_name| replace:: %(product_name)s
""" % { "lorem_ipsum": lorem_ipsum, "inputs_required": inputs_required, "product_name": product_name, }

# -- Options for HTML output -------------------------------------------------

openapi_default_renderer='httpdomain'

#html_sidebars = { '**': ['globaltoc.html', 'searchbox.html', 'relations.html'] }

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
#html_theme = 'sphinx_typo3_theme'
#html_theme = 'sphinx_material'
#html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = 'HTML Title'
html_logo = "_static/puttshack-logo-schema.png"
html_favicon = "_static/favicon.ico"
html_css_files = ["theme_overrides.css"]

html_theme_options = {

    # -- material theme options -----------------------------------------------

    # Set the name of the project to appear in the navigation.
    #'nav_title': 'Descriptive{Puttshack} APIs',

    # Set you GA account ID to enable tracking
    #'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    #'base_url': 'https://project.github.io/project',

    # Set the color and the accent color
    #'color_primary': 'purple',
    #'color_accent': 'light-purple',

    # Set the repo location to get a badge with stats
    #'repo_url': 'https://github.com/project/project/',
    #'repo_name': 'Puttshack',

    # Visible levels of the global TOC; -1 means unlimited
    #'globaltoc_depth': -1,

    # If False, expand all TOC entries
    #'globaltoc_collapse': True,

    # If True, show hidden TOC entries
    #'globaltoc_includehidden': False,

    # -- Typo3 theme options --------------------------------------------------

    #'logo': 'puttshack.png',

    # -- Sphinx Book Theme Configurations -------------------------------------
    'navbar_footer_text': 'Last updated on: ' + dt_string+ ' <a style="font-style: italic;" href="https://chrissm79.github.io/puttshack-cloud/">based on Swagger API specifications</a>',
    'use_download_button': False,
    'use_fullscreen_button': False,
    'logo_only': True,

    # -- pydata theme options -------------------------------------------------
    'show_toc_level': '2',
    # the following field in pydata theme config is deprecated
    #'search_bar_position': 'navbar',
    #'navbar_end': 'search-field.html',
}

# -- Redoc / Swagger API generation configuration

redoc = [
    {
        'name': 'Puttshack Cloud API (Redoc Layout)',
        'page': 'puttshack-apis/index',
        'spec': 'api_spec/swagger.json',
        'embed': True,
        'opts': {
        'lazy-rendering': True,
        'suppress-warnings': True,
        'hide-hostname': False,
        'expand-responses': [ ],
        },
    },
]

