# mapreduce.split
# Performs splitting of large files for input to multiple processes.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Mon Sep 07 18:18:14 2015 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see LICENSE.txt
#
# ID: split.py [] benjamin@bengfort.com $

"""
Performs splitting of large files for input to multiple processes.
"""

##########################################################################
## Imports
##########################################################################

import os
import string

##########################################################################
## Splitter
##########################################################################

class Splitter(object):
    """
    Generic splitter object that performs file splitting to a directory by
    number of chunks, Rabin-Karp, max file size, etc.
    """

    def __init__(self, chunks, **options):
        self.chunks  = chunks
        self.options = options

    def get_output_path(self, inpath, part=0, directory=None, prefix=None):
        """
        Computes and returns the output path from the original path name.
        """
        # Gather parts of the path
        prefix    = prefix or self.options.get('prefix', None)
        directory = directory or os.path.dirname(inpath)
        name, ext = os.path.splitext(os.path.basename(inpath))

        # Make directory if it does not exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Compute path from input and return
        fname = "{}-{}{}".format(name, part, ext)
        if prefix:
            fname = "{}-{}".format(prefix, fname)

        return os.path.join(directory, fname)

    def split(self, inpath, outdir, buffer_size=16384):
        """
        Splits an input file into multiple chunks based on an even number of
        chunks (the default in this case). It writes the given chunks to
        split files contained in the outdir.

        TODO: clean up and make better
        """

        # Compute the block size based on the # of chunks
        size  = os.stat(inpath).st_size
        block = (size / self.chunks) + 1

        # Create first output file
        fp = open(self.get_output_path(inpath, 0, outdir), 'w+')
        fp.write("0\n")

        # Read through chunks of input data and write to splits.
        idx = 0 # character index
        mdx = 1 # block index
        for chunk in self.read(inpath, buffer_size):
            for char in chunk:
                fp.write(char)
                idx += 1

                if (char in string.whitespace) and (idx > block * mdx):
                    # Close current split and open new one.
                    fp.close()
                    mdx += 1
                    fp = open(self.get_output_path(inpath, mdx-1, outdir), 'w+')
                    fp.write(str(idx) + "\n")

        # Ensure that current pointer is closed
        fp.close()

    def read(self, path, buffer_size=16384):
        """
        Reads a file loading only the buffer size into memory at a time.
        """
        with open(path, 'rb') as fp:
            chunk = fp.read(buffer_size)
            while chunk:
                yield chunk
                chunk = fp.read(buffer_size)
