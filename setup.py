#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='slowo',
    version='0.2',
    description='A python implentación of advanced uwuification.',
    license="GPLv3",
    author='Gintautas Kazlauskas',
    author_email='gintautaskazlauskas@protonmail.com',
    url="https://www.github.com/gitautas/slowo",
    package_dir = {
        "": "src"
    },
    packages=["slowo"],  #same as name
    install_requires=['wheel'], #external packages as dependencies
    scripts=[]
)
