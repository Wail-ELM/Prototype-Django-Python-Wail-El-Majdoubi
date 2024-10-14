# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

# **Corrected path:**
sys.path.insert(0, os.path.abspath('C:/Users/wail1/Desktop/MULTIMEDIA SCHOOLMAP/Prototype-Django-Python-Wail-El-Majdoubi/myproject_python')) 

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject_python.settings")
django.setup()

project = 'Prototype 1 Python/Django - Blog'
copyright = '2024, Wail El Majdoubi'
author = 'Wail El Majdoubi'
release = '14/10/2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False