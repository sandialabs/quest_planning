import os
import sys

# Debug print to verify paths
print("sys.path before insertion:", sys.path)
sys.path.insert(0, os.path.abspath('C:\\Users\\aslopez\\Python-Projects'))
print("sys.path after insertion:", sys.path)

project = 'QuESt Planning'
author = 'Cody Newlun'
release = '0.1.0'

extensions = [

    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    ]


templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
