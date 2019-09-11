import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='handset-utils',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/viarurla/handset-utils',
    license='MIT License',
    author='Oliver Jacobs',
    author_email='OliverJacobs@Protonmail.com',
    description='Utility to query either a database or api and generate a sim equipped handset object',
    long_description=README,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.22.0'
    ],
)

