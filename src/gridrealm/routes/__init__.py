"""Gridrealm Routes package."""
# Copyright Curtis Sand, Dennison Gaetz - 2018

from enum import Enum

from .core import register_views

from .index import Index
from .logout import Logout
from .assets import Assets
from .docs import Docs
from .favicon import Favicon
from .sysmsg import SysMsg


class Views(Enum):
    """Enum of all the non-API View classes for gridrealm."""

    index = Index
    logout = Logout
    assets = Assets
    docs = Docs
    favicon = Favicon
    sysmsg = SysMsg
