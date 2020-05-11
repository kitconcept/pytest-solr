# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)


def read(fname):
    return open(os.path.join(here, fname)).read()


setup(
    name='pytest-solr',
    version='1.0.0',
    description='Solr process and client fixtures for py.test.',
    long_description=(
        read('README.rst') + '\n\n' + read('CHANGES.rst')
    ),
    keywords='tests py.test pytest fixture solr',
    author='kitconcept GmbH',
    author_email='info@kitconcept.com',
    url='https://github.com/kitconcept/pytest-solr',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'pytest>=3.0.0',
        'pysolr',
    ],
    tests_require=[
        'pytest-cov',
        'pytest-xdist',
        'mock',
    ],
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    extras_require={},
    entry_points={
        'pytest11': [
            'pytest_solr = pytest_solr.plugin'
        ]},
)
