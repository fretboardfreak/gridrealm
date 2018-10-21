#!/usr/bin/env python
"""Compile PlantUML text files into UML images."""

import sys
import argparse
from plantuml import PlantUML

VERSION = "0.1"
VERBOSE = False
DEBUG = False


def main():
    """Compile the input files into UML images."""
    args = parse_cmd_line()
    dprint(args)
    outfile = '.'.join(args.input.name.split('.')[:-1] + [args.suffix])
    vprint('Parsing "%s" to "%s"' % (args.input.name, outfile))
    puml = PlantUML()
    return puml.processes_file(args.input.name, outfile=outfile)


def parse_cmd_line():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--version', help='Print the version and exit.', action='version',
        version='%(prog)s {}'.format(VERSION))
    DebugAction.add_parser_argument(parser)
    VerboseAction.add_parser_argument(parser)
    parser.add_argument('input', type=open,
                        help="The input PlantUML file to process.")
    parser.add_argument('-s', '--suffix', default="png",
                        help="The suffix to use for the output file.")
    return parser.parse_args()


def dprint(msg):
    """Conditionally print a debug message."""
    if DEBUG:
        print(msg)


def vprint(msg):
    """Conditionally print a verbose message."""
    if VERBOSE:
        print(msg)


class DebugAction(argparse.Action):
    """Enable the debugging output mechanism."""

    flag = '--debug'
    help = 'Enable debugging output.'

    @classmethod
    def add_parser_argument(cls, parser):
        """Add the argument for this action to the parser."""
        parser.add_argument(cls.flag, help=cls.help, action=cls)

    def __init__(self, option_strings, dest, **kwargs):
        """Initialize the action, redefining some default options."""
        super(DebugAction, self).__init__(option_strings, dest, nargs=0,
                                          default=False, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        """Enable the debugging option."""
        print('Enabling debugging output.')
        global DEBUG
        DEBUG = True
        setattr(namespace, self.dest, True)


class VerboseAction(DebugAction):
    """Enable the verbose output mechanism."""

    flag = '--verbose'
    help = 'Enable verbose output.'

    def __call__(self, parser, namespace, values, option_string=None):
        """Enable the verbose option."""
        print('Enabling verbose output.')
        global VERBOSE
        VERBOSE = True
        setattr(namespace, self.dest, True)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        sys.exit(0)
    except KeyboardInterrupt:
        print('...interrupted by user, exiting.')
        sys.exit(1)
    except Exception as exc:
        if DEBUG:
            raise
        else:
            print('Unhandled Error:\n{}'.format(exc))
            sys.exit(1)
