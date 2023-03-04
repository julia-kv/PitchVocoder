#!/usr/bin/env python
from setuptools import find_packages, setup

requirements_path = 'requirements.txt'
with open(requirements_path) as f:
    required = f.read().splitlines()

setup(
    name='stretch time audio',
    packages=find_packages(),
    version='0.1.0',
    description='algorithm for changing the time of an audio recording without changing the pitch',
    author='Korpusova Julia',
    install_requires=required,
    license='VK Internship',
)
