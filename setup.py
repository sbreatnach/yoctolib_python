#!/usr/bin/env python
"""
PyPi installation script for the project
"""
# HACK: for issue https://bugs.python.org/issue8876 which is fixed but may not
# have filtered down for your particular distro
import os
del os.link

from setuptools import setup

setup(
    name='yoctopuce',
    version='1.10.24182',
    author='',
    author_email='',
    description='',
    license='Proprietary',
    keywords='yoctopuce watchdog',
    url='https://github.com/yoctopuce/yoctolib_python',
    package_dir={'': 'Sources'},
    packages=[''],
    include_package_data=True,
    install_requires=[],
    long_description='',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
