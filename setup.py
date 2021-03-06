#!/bin/env python
# -*- coding: utf-8 -*
"""

    @FileName: setup.py
    @Author: liuxuan05
    @CreatTime: 2014-10-22 13:25:59
    @LastModif: 2014-10-22 13:54:37
    @Note:
"""

import os
import re
import sys
import textwrap
import traceback
from distutils.core import setup

try:
    # pylint: disable=W0622
    __name__ = 'cup'
    __author__ = __import__(__name__).version.AUTHOR
    __version__ = __import__(__name__).version.VERSION
# pylint: disable=W0703
except Exception:
    print traceback.print_exc()
    exit(-1)


# Guannan add windows platform support on 2014/11/4 20:04
def _find_packages(prefix=''):
    packages = []
    path = '.'
    prefix = prefix
    for root, _, files in os.walk(path):
        if '__init__.py' in files:
            if sys.platform.startswith('linux'):
                packages.append(
                    re.sub('^[^A-z0-9_]', '', root.replace('/', '.'))
                )
            elif sys.platform.startswith('win'):
                packages.append(
                    re.sub('^[^A-z0-9_]', '', root.replace('\\', '.'))
                )
    print packages
    return packages


setup(
    name=__name__,
    version=__version__,
    description='A common useful python library',
    long_description=(
        'Wish CUP to be a popular common useful python-lib in the world! '
        '(Currently, Most popular python lib in baidu)'
    ),
    url='https://github.com/baidu/CUP/',
    author=__author__,
    maintainer='Guannan Ma mythmgn@gmail.com @mythmgn',
    author_email='mythmgn@gmail.com',
    classifiers=textwrap.dedent("""
        Development Status :: 5 - Production/Stable
        Intended Audience :: Developers
        License :: OSI Approved ::  Apache License Version 2
        Operating System :: Linux Macos Unix
        Programming Language :: Python :: 2.6
        Programming Language :: Python :: 2.7
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Utilities
        """).strip().splitlines(),
    license='Apache 2',
    keywords='library common',
    packages=_find_packages(__name__),
    package_data={'': ['*.so']}
)

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
