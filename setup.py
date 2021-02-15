#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# Build setup.
setup(
    name="python-package",
    version="0.0.1",
    author="Jasmina Dzurlic",
    author_email="jd34519@columbia.edu",
    description="A packages that determines the current day of the week.",
    entry_points={
        "console_scripts": ["day_of_the_week = python-package.__main__:main"]
    },
)