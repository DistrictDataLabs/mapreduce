# mapreduce.job
# Defines a MapReduce job and parallel execution context.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Fri Sep 04 10:57:16 2015 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see LICENSE.txt
#
# ID:job.py [] benjamin@bengfort.com $

"""
Defines a MapReduce job and parallel execution context.
"""

##########################################################################
## Imports
##########################################################################

import os
import sys
import pickle

from multiprocessing import Pool

##########################################################################
## MapReduce Job Class
##########################################################################

class Job(object):

    def __init__(self, mapper, reducer, input=sys.stdin, output=sys.stdout,
                 map_tasks=None, reduce_tasks=None, **options):
        """
        Defines the job configuration for Mapreduce by passing in a mapper
        class and a reducer class (or a callable that accepts key/values).
        """
        self.mapper   = mapper
        self.reducer  = reducer
        self.input    = input
        self.output   = output
        self.maptasks = map_tasks
        self.redtasks = reduce_tasks
        self.options  = options

    
