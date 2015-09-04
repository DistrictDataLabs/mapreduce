# tests
# Testing for the mapreduce module
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Fri Sep 04 10:48:59 2015 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the mapreduce module
"""

##########################################################################
## Imports
##########################################################################

import os
import unittest

##########################################################################
## Fixtures
##########################################################################

EXPECTED_VERSION = "0.1"

##########################################################################
## Initialization Tests
##########################################################################

class InitializationTest(unittest.TestCase):

    def test_initialization(self):
        """
        Assert the world is sane and 2+2=4
        """
        self.assertEqual(2+2, 4)

    def test_import(self):
        """
        Assert that we can import the inigo library
        """
        try:
            import mapreduce
        except ImportError:
            self.fail("Could not import the mapreduce library")

    def test_version(self):
        """
        Check the expected version matches
        """
        import mapreduce
        self.assertEqual(mapreduce.__version__, EXPECTED_VERSION)

    def test_version_extract(self):
        """
        Test the setup.py method of extracting the version
        """
        namespace = {}
        versfile = os.path.join(
            os.path.dirname(__file__), "..", "mapreduce", "__init__.py"
        )

        with open(versfile, 'r') as versf:
            exec(versf.read(), namespace)

        self.assertEqual(namespace['get_version'](), EXPECTED_VERSION)
