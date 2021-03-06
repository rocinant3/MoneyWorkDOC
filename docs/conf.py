# -*- coding: utf-8 -*-
#
# Django Kong documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 18 09:17:59 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.intersphinx', 'sphinxcontrib.mermaid']
templates_path = ['_templates']

# Add any paths that contain templates here, relative to this directory.

# The suffix of source filenames.
source_suffix = '.rst'
html_static_path = ['_static']

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MoneyWork'
copyright = u'2021, rocinante'

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'nature'
htmlhelp_basename = 'MoneyWorkDOC'

pygments_style = 'sphinx'

html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': '\\usepackage[utf8]{inputenc}',
    'babel': '\\usepackage[russian]{babel}',
    'cmappkg': '\\usepackage{cmap}',
    'fontenc': '\usepackage[T1,T2A]{fontenc}',
    'utf8extra': '\\DeclareUnicodeCharacter{00A0}{\\nobreakspace}',
}


latex_documents = [
    ('index', 'Sphinx.tex', u'????????????????????????',
     u'???????????? ????????????????', 'manual'),
]
