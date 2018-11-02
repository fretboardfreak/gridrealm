"""Gridrealm Configuration."""

# Originally borrowed from
# https://github.com/fretboardfreak/netify/master/src/netify/config.py
# Original Author: Curtis Sand

# Modifications: Copyright 2018 - Curtis Sand, Dennison Gaetz

import os
from configparser import SafeConfigParser
from enum import Enum
from attrdict import AttrDict


class Singleton(type):
    """Base class for Singleton objects."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Return the existing Singleton instance or create a new one."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


def guess_a_config_location():
    """Try to look for a gridrealm config file in a few appropriate places."""
    names = ['gridrealm.cfg', 'gr.cfg', 'config.cfg', 'dev.cfg']
    home_paths = [os.path.join(os.getenv('HOME'), stub)
                  for stub in ['.%s', 'gridrealm/%s']]
    other_paths = ['/etc/gridrealm/%s']
    paths = [os.path.join(os.getcwd(), name) for name in names]
    paths.append('/etc/gridrealm.cfg')
    for name in names:
        paths.extend(path % name for path in home_paths)
    for name in names:  # second loop to enforce list order
        paths.extend(path % name for path in other_paths)
    return [path for path in paths if os.path.exists(path)]


class Config(metaclass=Singleton):
    """The config object providing access to gridrealm configuration."""

    default_secret_key_size = 64  # 64 bytes => 512 bits

    def __init__(self, config_file=None):
        """Open and read the configuration file from disk."""
        self.file = config_file
        self.parser = SafeConfigParser()
        if isinstance(self.file, (str, list)):
            self.parser.read(self.file)
        else:  # assume file object was given instead
            self.parser.read_file(self.file)
        self._flask_cache = None
        self._assets_cache = None

    def get(self, section, option, fallback=None):
        """Get an Option from one of the Config Sections."""
        if not fallback:  # attempt to get default value as fallback
            try:
                fallback = Section[section].value[option].value
            except KeyError:  # no default value for this option
                fallback = None
        return self.parser.get(section, option, fallback=fallback)

    def to_string_dict(self):
        """Return the whole config as a dictionary of string key values.

        All keys and values are strings, as written in the config file.
        """
        ret_val = {}
        for section in self.parser.sections():
            for option in self.parser.options(section):
                sect = ret_val.get(section, {})
                sect[option] = self.parser.get(section, option)
                ret_val[section] = sect
        return ret_val

    @classmethod
    def get_random_secret_key(cls, size=None):
        """Generate a random secret key string."""
        if not size:
            size = cls.default_secret_key_size
        return os.urandom(size)

    @property
    def flask_config_dict(self):
        """Parse the config file and create a dict compatible with Flask."""
        if self._flask_cache:
            return self._flask_cache
        self._flask_cache = dict([(obj.name, obj.value)
                                  for obj in FlaskDefaults])
        for option in self.parser.options(Section.flask.name):
            self._flask_cache[option.upper()] = self.get(Section.flask.name,
                                                         option)
        return self._flask_cache

    def update_flask(self, flask_app):
        """Add the options from the Flask section into the flask object."""
        flask_app.config.update(self.flask_config_dict)

    def _section_as_dict(self, section):
        """Parse a config section into a python dictionary."""
        options = {}
        if not self.parser.has_section(section):
            return options
        for option in self.parser.options(section):
            # Don't know which options might be boolean so we can't use
            # self.parser.getboolean()
            tmp = self.get(section, option)
            if str(tmp).lower() in ['yes', 'y', 'true', 't']:
                options[option] = True
            elif str(tmp).lower() in ['no', 'n', 'false', 'f']:
                options[option] = False
            else:
                options[option] = str(tmp)
        return options

    @property
    def assets(self):
        """Get the 'assets' section as an AttrDict."""
        if self._assets_cache:
            return self._assets_cache
        asset_defaults = Section.assets.value
        ret_val = dict([(obj.name, obj.value) for obj in asset_defaults])
        ret_val.update(self._section_as_dict(Section.assets.name))
        self._assets_cache = AttrDict(**ret_val)
        return self._assets_cache


class FlaskDefaults(Enum):
    """Default values for the Flask section of the config file."""

    SECRET_KEY = Config.get_random_secret_key()
    LOGGER_NAME = 'gridrealm'


class AssetsDefaults(Enum):
    """Default values for the assets section of the config file."""

    asset_path = "_assets"
    css_stub = "client/css/%s"
    js_stub = "client/js/%s"
    asset_stub = "_assets/%s"
    asset_uri = '_assets'
    docs_stub = "docs/%s"
    favicon_uri = os.path.join(asset_path, "images/favicon.ico")
    client_uri = "client.html"
    landing_uri = "landing.html"


class Section(Enum):
    """String names for the sections in the gridrealm config file."""

    flask = FlaskDefaults
    assets = AssetsDefaults
