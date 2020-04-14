import os
import sys
from distutils.util import convert_path

sys.path.append(os.getcwd())

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

main_ = {}
ver_path = convert_path('beatmap/__init__.py')
with open(ver_path) as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, main_)

setup(
    name='beatmap',
    description='A tool for determining the valid P/P0 range in BET isotherms',
    zip_safe=False,
    long_description_content_type="text/x-rst",
    version=main_['__version__'],
    classifiers=['Development Status :: 2 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Physics'],
    packages=['beatmap',],
    install_requires=['numpy',
                      'scipy',
                      'matplotlib'],
    author='Jeff Gostick',
    author_email='jgostick@uwaterloo.ca',
    url='http://pmeal.org',
    project_urls={
        'Documentation': 'https://beatmap.readthedocs.io/en/master/',
        'Source': 'https://github.com/PMEAL/beatmap/',
        'Tracker': 'https://github.com/PMEAL/beatmap/issues',
    },
)
