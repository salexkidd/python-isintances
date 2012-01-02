# -*- coding:utf-8 -*-
from setuptools import setup
from setuptools import find_packages

from isinstances import __version__
from isinstances import __license__
from isinstances import __author__
import isinstances
import sys

sys.path.append('./isinstances')
sys.path.append('./tests')


setup(
    name="python-isinstances",
    author=__author__,
    author_email="salexkidd@gmail.com",
    version=__version__,
    packages=find_packages(),
    description="isinstances",
    long_description=isinstances.__doc__,
    url="https://github.com/salexkidd/python_isinstances",
    keywords='isinstance object',
    license=__license__,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Utilities",
        ],
    test_suite="t.isinstancesTestSuite",
    )
