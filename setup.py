#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages


VERSION = '0.1.2'
REQS = [
    'click',
    'pysocks',
    'telethon',
    'python-dateutil',
    'peewee',
]


setup(
    name='zs',
    version=VERSION,
    description='',
    license='MIT',
    packages=find_packages(),
    install_requires=REQS,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['zs-tg=zs.cli:telegram'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
