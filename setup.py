from pathlib import Path

from setuptools import find_packages, setup

classes = """
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: 3.10
    Programming Language :: Python :: 3.11
    Programming Language :: Python :: 3.12
    Programming Language :: Python :: 3.13
    Programming Language :: Python :: 3.14
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Operating System :: OS Independent
"""
classifiers = [classifier.strip() for classifier in classes.splitlines() if classifier]

setup(
    name='version-plus',
    version='1.7.0',
    description='The + / ++ / +++ release tool for multi-file projects',
    long_description=Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    author='Adam Schubert',
    author_email='adam.schubert@sg1-game.net',
    url='https://github.com/Salamek/version',
    project_urls={
        'Source': 'https://github.com/Salamek/version',
        'Issues': 'https://github.com/Salamek/version/issues',
    },
    license='GPL-3.0',
    classifiers=classifiers,
    keywords=['release', 'release-automation', 'semantic-versioning', 'semver', 'version', 'version-bump'],
    python_requires='>=3.9',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'packaging',
        'docopt',
        'pyyaml',
        'gitpython',
    ],
    entry_points={
        'console_scripts': [
            'version = version.__main__:main',
        ],
    }
)
