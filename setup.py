from setuptools import setup

long_description = """
This is a package that describes some basic data structures implementated
in Python.
"""


setup(
    name="data-structures",
    version="0.1-dev",
    long_description=long_description,
    url='http://github.com/lordsheepy/data-structures',
    author='Stephen Babineau',
    author_email='tien_ralter@hotmail.com',
    #insert license here
    packages=['data_structures'],
    #or setuptools.find_packages(exclude=['tests'])
    install_requires=['setuptools', ],
)
