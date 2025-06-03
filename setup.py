from setuptools import setup, find_packages

DISTNAME = "quest_planning"
VERSION = "1.0"
PYTHON_REQUIRES = ">=3.6"#, <3.11"
DESCRIPTION = "Sandia National Laboratories Energy Storage Application Platform"
LONG_DESCRIPTION = open("README.md").read()
AUTHOR = "Sandia National Laboratories"
MAINTAINER_EMAIL = "cjnewlu@sandia.gov"
LICENSE = "BSD 3-clause"
URL = "https://github.com/sandialabs/quest_planning.git"


setup(
    name=DISTNAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    python_requires=PYTHON_REQUIRES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    url=URL,
    install_requires=[
        "branca==0.7.1",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "contourpy==1.2.0",
        "cycler==0.12.1",
        "et-xmlfile==1.1.0",
        "folium==0.16.0",
        "fonttools==4.50.0",
        "geopandas==1.0.1",
        "gurobipy==11.0.1",
        "idna==3.6",
        "Jinja2==3.1.3",
        "kiwisolver==1.4.5",
        "Markdown==3.7",
        "MarkupSafe==2.1.5",
        "matplotlib==3.8.3",
        "narwhals==1.39.0",
        "networkx==3.2.1",
        "nose==1.3.7",
        "numpy==1.26.4",
        "openpyxl==3.1.2",
        "packaging==24.0",
        "pandas==2.2.1",
        "pillow==10.2.0",
        "plotly==6.0.1",
        "ply==3.11",
        "Pyomo==6.7.1",
        "pyparsing==3.1.2",
        "PySide6==6.5.2",
        "PySide6-Addons==6.5.2",
        "PySide6-Essentials==6.5.2",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.1",
        "PyUtilib==6.0.0",
        "pyYAML==6.0.1",
        "requests==2.31.0",
        "shiboken6==6.5.2",
        "six==1.16.0",
        "tzdata==2024.1",
        "urllib3==2.2.1",
        "xyzservices==2023.10.1",
    ],

    package_data={
        '': ['*.txt', '*.rst', '*.json', '*.jpg', '*.qss', '*.sh', '*.svg', '*.png', '*.kv', '*.bat', '*.csv', '*.md', '*.yml', '*.dll', '*.idf', '*.doctree', '.*info', '*.html', '*.js', '*.inv', '*.gif', '*.css', '*.eps', '*.pickle', '*.xlsx', '*.ttf', '*.pdf', '**/license*', '*.yml', '*.ui', '*.eot', '*.woff', '*.woff2', 'LICENSE', '*.mplstyle', '*.ini' ],
    },

    entry_points={
        'console_scripts': [
            'quest_planning = quest_planning.__main__:main'
        ]
    }
)
