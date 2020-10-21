=================
Pattern Singleton
=================

.. image:: https://img.shields.io/pypi/pyversions/pattern_singleton
        :target: https://pypi.python.org/pypi/pattern_singleton
        :alt: Python

.. image:: https://img.shields.io/pypi/v/pattern_singleton.svg?color=brightgreen
        :target: https://pypi.python.org/pypi/pattern_singleton
        :alt: PyPi

.. image:: https://img.shields.io/pypi/l/pattern_singleton?color=brightgreen
        :target: https://github.com/MarcinMysliwiec/pattern_singleton/blob/master/LICENSE
        :alt: License

.. image:: https://travis-ci.com/MarcinMysliwiec/pattern_singleton.svg
        :target: https://travis-ci.com/MarcinMysliwiec/pattern_singleton
        :alt: Build

.. image:: https://codecov.io/gh/MarcinMysliwiec/pattern_singleton/branch/master/graph/badge.svg?token=ZJCBWXAJPR
        :target: https://codecov.io/gh/MarcinMysliwiec/pattern_singleton
        :alt: Coverage

Description
~~~~~~~~~~~~

My implementation of Singleton Design Pattern based on metaclass method.


* Free software: `MIT <https://github.com/MarcinMysliwiec/pattern_singleton/blob/master/LICENSE>`__ license
* But I would appreciate a star on `GitHub <https://github.com/MarcinMysliwiec>`__

Installation
~~~~~~~~~~~~

Just use (No other package is needed):

.. code-block:: sh

    $ pip install pattern-singleton


Example Usage
~~~~~~~~~~~~~

.. code-block:: python

    from pattern_singleton import Singleton


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
