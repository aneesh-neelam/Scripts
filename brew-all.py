#!/usr/bin/env python3

"""
Script uses brew, for Homebrew on macOS
"""

import sys
from subprocess import call


def brew_update():
    status = call([
        'brew',
        'update',
    ])
    return status


def brew_upgrade():
    status = call([
        'brew',
        'upgrade',
    ])
    return status


def brew_cask_upgrade():
    status = call([
        'brew',
        'cask',
        'upgrade',
    ])
    return status


def handle_status(status):
    if status != 0:
        sys.exit(status)


def main():
    status = brew_update()
    handle_status(status)

    status = brew_upgrade()
    handle_status(status)

    status = brew_cask_upgrade()
    handle_status(status)

    sys.exit(0)


if __name__ == '__main__':
    main()
