"""Gridrealm Utilities."""

import time

TS_FORMAT = '%Y%m%d-%H%M%S'

def ts_to_str(timestamp=None):
    """Convert a float timestamp into a string."""
    return time.strftime(TS_FORMAT, time.gmtime(timestamp))
