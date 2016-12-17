import inspect

from collections import namedtuple, defaultdict
from functools import wraps

from typing import Callable


Trace = namedtuple('Trace', ['ret', 'args', 'kwargs'])
result = defaultdict(list)


def collect(func: Callable) -> Callable:
    @wraps(func)
    def _collect(*args, **kwargs):
        ret = func(*args, **kwargs)
        func_module = inspect.getmodule(func)
        key = '{}.{}'.format(func_module.__name__, func.__name__)
        result[key].append(Trace(ret=ret, args=args, kwargs=kwargs))
        return ret

    return _collect
