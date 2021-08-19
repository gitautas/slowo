#!/usr/bin/env python3
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='slowo',
   version='0.1',
   description='A python implentación of advanced uwuification.',
   license="GPLv3",
   author='Gintautas Kazlauskas',
   author_email='gintautaskazlauskas@protonmail.com',
   url="uwu.lt",
   packages=['foo'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)
