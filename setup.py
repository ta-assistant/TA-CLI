from os import name
from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


setup(
    name="assist",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points="""
    [console_scripts]
    assist=assist.cli:cli
    """
)
