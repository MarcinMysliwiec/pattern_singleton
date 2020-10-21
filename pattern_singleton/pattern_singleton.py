"""Main module."""
import threading

lock = threading.Lock()


class Singleton(type):
    """
    The Singleton class can be implemented in different
    ways in Python. This method is using metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__`
        argument do not affect the returned instance.
        """
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
