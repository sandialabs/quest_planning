import os
import sys

# Debug print to verify paths
print("sys.path before insertion:", sys.path)
# Add the `quest_planning` root directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
print("sys.path after insertion:", sys.path)

project = 'QuESt Planning'
author = 'Cody Newlun'
release = '1.0.0'

extensions = [

    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'myst_parser',
    ]

myst_enable_extensions = ["linkify", "html_admonition", "html_image"]

autodoc_mock_imports = ["geopandas", "plotly"]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['images']
html_extra_path = ['images']
html_baseurl = "https://sandialabs.github.io/quest_planning/"
