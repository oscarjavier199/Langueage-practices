
from setuptools import setup

setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='Oscar Perez',
    author_email='oscarjavier2@proton.me',
    packages=['my_package'],
    install_requires=[
        'numpy',
        'pandas',
    ],
)