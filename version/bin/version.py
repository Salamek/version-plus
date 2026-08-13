#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main entry-point into the 'version' application.

Update project version files and optionally commit, tag, and push a release.

License: GPL-3.0
Website: https://github.com/Salamek/version

Command details:
    init                Detect common version files and create .version.yml.
    mark                Mark project specified by --project_dir by <version>.
    status              Show current --project_dir version.
    changelog           Changelog.


Usage:
    version init [-p DIR] [-c FILE] [--force]
    version mark <version> [-p DIR] [-c FILE] [--dry] [--all_yes] [--force]
    version status [-p DIR] [-c FILE]
    version changelog info
    version changelog generate <from_version> <to_version> [--dry]
    version 
    version <version> [-p DIR] [-c FILE] [--dry] [--all_yes] [--force]
    version (-h | --help)
    version (-v | --version)

Options:
    --dry                       Preview the release without changing anything.
    -p DIR --project_dir=DIR    Project directory, if not set current is used.
    -y --all_yes                Answer YES to all prompts.
    -f --force                  Force command when possible.
    -c FILE --config_file=FILE  Path to config file; defaults to DIR/.version.yml.
    --version                   Show version.
"""
import signal
import sys
import logging
from version.Version import Version
from version.StrictVersion import StrictVersion
from version.exception import ProjectVersionError, ConfigurationError
from version.logging.ColoredFormatter import ColoredFormatter
from version.initializer import initialize_project

from docopt import docopt

from version import __version__
logging_level = logging.INFO
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging_level)
fmt = '[%(levelname)-19s] %(message)s'
datefmt = '%m%d %H:%M:%S'
console_handler.setFormatter(ColoredFormatter(fmt, datefmt))

LOG = logging.getLogger()
LOG.setLevel(logging_level)
LOG.addHandler(console_handler)


def main() -> None:
    """
    Main entry point
    :return: 
    """
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))  # Properly handle Control+C
    options = docopt(__doc__, version=__version__)

    try:
        if options['init']:
            config_path = initialize_project(options)
            print('Created {}'.format(config_path))
            print('Review it, then preview your first release with `version + --dry`.')
            return

        version = Version(options)

        LOG.info('Current working directory is {}'.format(version.get_project_dir()))
        LOG.info('Current configuration is from {}'.format(version.get_config_file()))
        LOG.debug('Current configuration is: {}'.format(version.get_config()))
        LOG.debug('Current options are: {}'.format(options))

        if options['<version>']:
            if options['<version>'] == 'mark':
                print('Please specify mark version')
            else:
                version.mark()
        elif options['changelog']:
            # Changelog CLI
            if options['info']:
                # Print info
                version.find_changelog()
            elif options['generate']:
                # Generate changelog

                if options['<to_version>'].lower() == 'head':
                    to_version = version.find_version()
                else:
                    to_version = StrictVersion(options['<to_version>'])

                if options['<from_version>'].lower() == 'changelog_head':
                    from_version = None
                else:
                    from_version = StrictVersion(options['<from_version>'])

                version.generate_change_log(to_version, from_version=from_version)

        elif not options['<version>'] or options['status']:
            version.status()
    except (ConfigurationError, ProjectVersionError) as error:
        if str(error):
            LOG.error(str(error))
        exit(1)
    except Exception:
        raise


if __name__ == '__main__':
    main()
