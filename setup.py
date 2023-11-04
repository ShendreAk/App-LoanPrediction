from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_path(file_path):
    with open(file_path, "rb") as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Akshay',
    author_email='akshay6720@gmail.com',
    packages= find_packages,
    install_requires = get_path("requirements.txt")
)


