#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from typing import List

from setuptools import find_packages, setup

# Package meta-data.
NAME = "pyfacebook"
PACKAGE = "pyfacebook"
DESCRIPTION = "Handler to send Facebook Messenger API."
URL = "https://github.com/luismayta/pyfacebook"
EMAIL = "slovacus@gmail.com"
AUTHOR = "@slovacus"


def find_version(fname: str) -> str:
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as filename:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in filename:
            match = reg.match(line)
            if match:
                version = match.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


__version__: str = find_version("pyfacebook/__init__.py")


def read(fname: str) -> str:
    with open(fname) as filename:
        content = filename.read()
    return content


required: List[str] = ["python-magic >= 0.4.13", "requests >=2.18.4", "verify >=1.1.1"]

setup(
    name=PACKAGE,
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    url=URL,
    license="BSD",
    packages=find_packages(exclude=["tests"]),
    install_requires=required,
    tests_require=[
        "pytest>=3.7.2",
        "PyHamcrest==1.10.1",
        "pytest-cov",
        "pytest-flask",
        "pytest-mock==1.9.0",
        "pytest-runner",
    ],
    extras_require={
        "docs": ["mock", "sphinx>=1.7.2"],
        "tests": [
            "sphinx",
            "pytest-cache",
            "pytest-cov",
            "pytest-flakes",
            "pytest-pep8",
            "pytest-runner",
            "jinja2",
            "pygments",
        ],
    },
    long_description=read("README.rst"),
    classifiers=["License :: OSI Approved :: BSD License"],
)
