#!/usr/bin/env python

"""
setuptools install script.
"""
from setuptools import setup, find_packages

from datacoco_ftp_tools import VERSION

requires = ["pysftp==0.2.9"]

setup(
    name="datacoco-ftp_tools",
    version=VERSION,
    author="Equinox Fitness",
    description="FTP tool wrapper",
    long_description=open("README.rst").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/equinoxfitness/datacoco-ftp_tools",
    scripts=[],
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
