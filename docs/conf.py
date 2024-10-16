# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Prototype 1 Python/Django - Blog - Wail El Majdoubi'
copyright = '2024, Wail El Majdoubi'
author = 'Wail El Majdoubi'
extensions = ['sphinx.ext.autodoc', 'sphinx_rtd_theme', 'sphinx.ext.napoleon'] 
html_theme = 'sphinx_rtd_theme'
release = '14/10/2024'

napoleon_google_docstring = True
napoleon_numpy_docstring = False

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
