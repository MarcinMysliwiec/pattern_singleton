#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Marcin Mysliwiec",
    author_email='marcin.mysliw@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Metaclass Singleton Pattern (supports Multi-thread).",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords=['pattern_singleton', 'singleton', 'design', 'pattern', 'metaclass', 'multi-thread'],
    name='pattern_singleton',
    packages=find_packages(include=['pattern_singleton', 'pattern_singleton.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/MarcinMysliwiec/pattern_singleton',
    version='1.2.0',
    zip_safe=False,
)
