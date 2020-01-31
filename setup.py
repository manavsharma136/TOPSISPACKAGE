# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="spytopsis",
    version="1.0.0",
    description="'Topsis analysis of a numeric csv file'",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/manavsharma136",
    author="Manav Sharma",
    author_email="manavsharma136@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["spy"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "spytopsis=spy.tab:main",
        ]
    },
)