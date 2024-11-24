from setuptools import setup
from setuptools import find_packages, setup

import json


with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='noawclg',
    version='0.0.8',
    url='https://github.com/reinanbr/noawclg',
    license='GPLv3',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='climate weather noaa',
    description=u'Library for getting dataset from noaa site',
    packages=find_packages(),
    install_requires=['xarray','netCDF4','matplotlib','geopy','openpyxl'],)
