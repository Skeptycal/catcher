#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" autosys package """
""" minimal requirements for SetupTools:

    from setuptools import setup, find_packages
    setup(
        name="HelloWorld",
        version="0.1",
        packages=find_packages(),
    )

    """


import os
from setuptools import find_packages
from setuptools import setup
import pkg_resources
import codecs
import re
here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="autosys",
    version="1.3.0",
    packages=find_packages(),
)

# def read(*parts):
#     with codecs.open(os.path.join(here, *parts), 'r') as fp:
#         return fp.read()


# def find_version(*file_paths):
#     version_file = read(*file_paths)
#     version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
#                               version_file, re.M)
#     if version_match:
#         return version_match.group(1)
#     raise RuntimeError("Unable to find version string.")


# pkg_resources.declare_namespace(__name__)
# assert pkg_resources.get_distribution('pip').version = '1.2.0'


# setup(
#     name=__name__,
#     version=find_version("autosys/version.py"),
#     description="System utilities for Python on macOS",
#     long_description=open("README.md").read(),
#     author="Michael Treanor",
#     author_email="skeptycal@gmail.com",
#     maintainer="Michael Treanor",
#     maintainer_email="skeptycal@gmail.com",
#     url="http://github.com/skeptycal/autosys/",
#     license="MIT",
#     include_package_data=True,
#     packages=["autosys"],
#     install_requires=[],
#     test_require=["tox", "pytest", "coverage", "pytest-cov"],
#     test_suite="test",
#     zip_safe=False,
#     keywords="cli utilities python ai ml text console log debug test testing",
#     classifiers=[
#         "Development Status :: 5 - Production/Stable",
#         "Environment :: Console",
#         "Environment :: MacOS X",
#         "Environment :: Web Environment",
#         "Framework :: Django",
#         "Framework :: Flask",
#         "Intended Audience :: Developers",
#         "License :: OSI Approved :: MIT License",
#         "Natural Language :: English",
#         "Operating System :: MacOS",
#         "Programming Language :: Cython",
#         "Programming Language :: Python :: 3.5",
#         "Programming Language :: Python :: 3.6",
#         "Programming Language :: Python :: 3.7",
#         "Programming Language :: Python :: Implementation :: CPython",
#         "Programming Language :: Python",
#         "Topic :: Software Development :: Libraries :: Python Modules",
#         "Topic :: Software Development :: Testing",
#         "Topic :: Utilities",
#     ],
# )
