#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open('requirements.txt') as rf:
    requirements = rf.readlines()

with open('test-requirements.txt') as rf:
    test_requirements = rf.readlines()

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='ucsmsdk',
    version='0.9.22',
    description="Python SDK for Cisco UCS",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author="Cisco Systems Inc",
    author_email='ucs-python@cisco.com',
    url='https://github.com/CiscoUcs/ucsmsdk',
    packages=[
        'ucsmsdk',
    ],
    package_dir={'ucsmsdk':
                 'ucsmsdk'},
    include_package_data=True,
    install_requires=requirements,
    license="http://www.apache.org/licenses/LICENSE-2.0",
    zip_safe=False,
    keywords='ucsmsdk',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    extras_require={
        'ssl': ['pyOpenSSL'],
        'docs': ['sphinx<1.3', 'sphinxcontrib-napoleon', 'sphinx_rtd_theme'],
    }
)
