import inspect
import importlib
import sys

from collections import namedtuple, defaultdict
from functools import wraps

from breaking_changes.inspector import public_interface

Trace = namedtuple('Trace', ['ret', 'args', 'kwargs'])
result = defaultdict(list)


def collect(func):
    @wraps(func)
    def _collect(*args, **kwargs):
        ret = func(*args, **kwargs)
        func_module = inspect.getmodule(func)
        key = '{}.{}'.format(func_module.__name__, func.__name__)
        result[key].append(Trace(ret=ret, args=args, kwargs=kwargs))
        return ret

    return _collect


def my_importer(modname):
    """Sample function that imports a module and returns it
    with all its functions decorated
    """
    mod = importlib.import_module(modname)
    # now get the functions
    interface = public_interface(mod)
    for func_name, func in interface:
        new_func = collect(func)
        setattr(mod, func_name, new_func)

    return mod


class DecorateOnImport(object):
    def find_module(self, fullname, path=None):
        return self

    def load_module(self, name):
        print("Loading module {}".format(name))
        return my_importer(name)
