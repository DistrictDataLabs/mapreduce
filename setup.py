# setup
# Implements the PyPI/setuptools setup and installation script.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Fri Sep 04 10:20:40 2015 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Implements the PyPI/setuptools setup and installation script.
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

# Read the __init__.py file for version info
version = None
versfile = os.path.join(os.path.dirname(__file__), "mapreduce", "__init__.py")
with open(versfile, 'r') as versf:
    exec(versf.read(), namespace)
    version = namespace['get_version']()

## Discover the packages
packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures", "register",))

## Load the requirements
requires = []
with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        line = line.strip()
        if line == '## Development Requirements': break
        if not line or line.startswith('#'): continue
        requires.append(line)

## Define the classifiers
classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
)

## Define the keywords
keywords = ('mapreduce', 'multiprocessing',)

## Define the description
long_description = ""

## Define the configuration
config = {
    "name": "Python MapReduce",
    "version": version,
    "description": "A multiprocess implementation of MapReduce in Python",
    "long_description": long_description,
    "license": "MIT",
    "author": "Benjamin Bengfort",
    "author_email": "bbengfort@districtdatalabs.com",
    "url": "https://github.com/districtdatalabs/mapreduce",
    "download_url": 'https://github.com/districtdatalabs/mapreduce/tarball/v%s' % version,
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "keywords": keywords,
    "zip_safe": True,
    "scripts": [],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
