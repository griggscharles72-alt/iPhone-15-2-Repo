from setuptools import setup, find_packages

setup(
    name="dr-core-shared",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyserial",
        "python-can",
        "scapy"
    ],
)
