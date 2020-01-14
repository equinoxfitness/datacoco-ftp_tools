#!/usr/bin/env python

"""
setuptools install script.
"""
import os
import re
from setuptools import setup, find_packages

requires = ["pysftp==0.2.9"]


def get_version():
    version_file = open(
        os.path.join("datacoco_ftp_tools", "__version__.py")
    )
    version_contents = version_file.read()
    return re.search('__version__ = "(.*?)"', version_contents).group(1)


setup(
    name="datacoco-ftp_tools",
    version=get_version(),
    author="Equinox Fitness",
    author_email='paul.singman@equinox.com',
    description="Data common code for ftp tools by Equinox",
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
