import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


setup(
    name='handset-utils',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/viarurla/handset-utils',
    license='MIT License',
    author='Oli.Jacobs',
    author_email='OliverJacobs@Protonmail.com',
    description='Utility to query either a database or api and generate a sim equipped handset object',
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'fonoapi>=0.1.2',
        'requests>=2.22.0'
    ]
)
