#!/usr/bin/env python

"""Tests for `pattern_singleton` package."""

import pytest

from pattern_singleton import Singleton


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


class Example(metaclass=Singleton):
    def __init__(self):
        self.variable = 1


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

    example_01 = Example()
    example_02 = Example()

    print(example_01.variable)  # displays 1
    print(example_02.variable)  # displays 1

    example_01.variable = 2  # changes value for every instance of Example class

    print(example_01.variable)  # displays 2
    print(example_02.variable)  # displays 2
