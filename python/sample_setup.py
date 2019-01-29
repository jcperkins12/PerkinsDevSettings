#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

install_requires = [
    "ffn",
    "lxml",
    "matplotlib",
    "numba",
    "numpy",
    "pandas",
    "requests",
    "scipy",
    "selenium",
]

dev_requires = ["black", "mypy"]


setup(
    name="MarketAnalysis",
    description="Analysis and study of the US markets using python",
    author="Cory Perkins",
    author_email="jcperkins12@gmail.com",
    version="0.0.1",
    url="https://jcperkins@bitbucket.org/jcperkins/market_analysis",
    license="MIT",
    packages=find_packages(),
    zip_safe=True,
    classifiers=["Programming Language :: Python :: 3.7"],
    install_requires=install_requires,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={"dev": dev_requires},
)
