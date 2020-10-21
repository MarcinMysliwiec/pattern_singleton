=================
Pattern Singleton
=================


.. image:: https://img.shields.io/pypi/v/pattern_singleton.svg
        :target: https://pypi.python.org/pypi/pattern_singleton
        :alt: PyPi

.. image:: https://img.shields.io/travis/MarcinMysliwiec/pattern_singleton.svg
        :target: https://travis-ci.com/MarcinMysliwiec/pattern_singleton
        :alt: Build

.. image:: https://codecov.io/gh/MarcinMysliwiec/pattern_singleton/branch/master/graph/badge.svg?token=ZJCBWXAJPR
        :target: https://codecov.io/gh/MarcinMysliwiec/pattern_singleton
        :alt: Coverage

.. image:: https://pyup.io/repos/github/MarcinMysliwiec/pattern_singleton/shield.svg
        :target: https://pyup.io/repos/github/MarcinMysliwiec/pattern_singleton/
        :alt: Updates


Description
~~~~~~~~~~~~

My implementation of Singleton Design Pattern based on metaclass method.


* Free software: MIT license
* Documentation: https://pattern-singleton.readthedocs.io.

Installation
~~~~~~~~~~~~

Just use (No other package is needed):

.. code-block:: sh

    $ pip install patternSingleton


Example Usage
~~~~~~~~~~~~~

.. code-block:: python

    from patternSingleton import Singleton


    class Example(metaclass=Singleton):
        def __init__(self):
            self.variable = 1


    if __name__ == '__main__':
        example_01 = Example()
        example_02 = Example()

        print(example_01.variable)  # displays 1
        print(example_02.variable)  # displays 1

        example_01.variable = 2     # changes value for every instance of Example class

        print(example_01.variable)  # displays 2
        print(example_02.variable)  # displays 2


Credits
-------

This package was created by `Marcin Mysliwiec <https://github.com/MarcinMysliwiec>`__ with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
