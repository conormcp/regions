# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This module provides a RegionList class.
"""

from astropy.io.registry import UnifiedReadWriteMethod

from .connect import RegionListRead, RegionListWrite
from .core import Region

__all__ = ['RegionList']


class RegionList:
    """
    Class to hold a list of `~regions.Region` objects.

    Parameters
    ----------
    regions : list of `~region.Region`
        The list of region objects.
    """

    # Unified I/O read and write methods
    read = UnifiedReadWriteMethod(RegionListRead)
    write = UnifiedReadWriteMethod(RegionListWrite)

    def __init__(self, regions):
        self.regions = regions

    def __getitem__(self, index):
        newregions = self.regions[index]
        if isinstance(newregions, Region):  # one item
            return newregions
        else:
            newcls = object.__new__(self.__class__)
            newcls.regions = newregions
            return newcls

    def __len__(self):
        return len(self.regions)

    def append(self, item):
        self.regions.append(item)

    def extend(self, item):
        self.regions.extend(item)

    def insert(self, index, item):
        self.regions.insert(index, item)

    def reverse(self):
        self.regions.reverse()

    def pop(self, index=-1):
        return self.regions.pop(index)

    def copy(self):
        newcls = object.__new__(self.__class__)
        newcls.regions = self.regions.copy()
        return newcls


# use list API docs for these methods
methods = ('append', 'extend', 'insert', 'reverse', 'pop', 'copy')
for method in methods:
    getattr(RegionList, method).__doc__ = getattr(list, method).__doc__
