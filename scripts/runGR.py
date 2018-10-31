#!/usr/bin/env python3
"""Run Gridrealm.

Note: this script must be placed inside a gridrealm dist directory or in a
python environment with the gridrealm engine installed.

"""

import sys

import gridrealm


if __name__ == '__main__':
    try:
        sys.exit(gridrealm.cli_main())
    except SystemExit:
        sys.exit(0)
    except KeyboardInterrupt:
        print('...interrupted by user, exiting.')
        sys.exit(1)
    except Exception as exc:
        print('Unhandled Error:\n{}'.format(exc))
        sys.exit(1)
