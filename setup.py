#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)


setup(
    name="perps",
    version="0.0.0",
    description="""Select a winner for the TCAP Raffle programmer""",
    long_description_content_type="text/markdown",
    author="Cryptex Finance",
    author_email="admin@cryptex.finance",
    include_package_data=True,
    install_requires=[
        "click>=8.1.8",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "web3>=7.8.0",
    ],
    python_requires=">=3.11.3",
    license="MIT",
    zip_safe=False,
    keywords="raffle",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.11",
    ],
)
