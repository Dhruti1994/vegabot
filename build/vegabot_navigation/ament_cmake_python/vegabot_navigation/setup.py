from setuptools import find_packages
from setuptools import setup

setup(
    name='vegabot_navigation',
    version='0.0.0',
    packages=find_packages(
        include=('vegabot_navigation', 'vegabot_navigation.*')),
)
