
from setuptools import setup, find_packages
from os import path

from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xcubia',
    version='0.1',
    description='A Site Connectivity Checker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kisekk David',
    author_email='cartpix@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='python requests monitor',

    packages=['xcubia', 'tests']

    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    package_data={
        'xcubia': ['xcubia.dat'],
    },

    scripts=['xcubia/bin/xcubia_script.py'],

)
