from collections import namedtuple, defaultdict
from functools import wraps

Trace = namedtuple('Trace', ['ret', 'args', 'kwargs'])
result = defaultdict(list)


def collect(func):
    @wraps(func)
    def _collect(*args, **kwargs):
        ret = func(*args, **kwargs)
        result[func].append(Trace(ret=ret, args=args, kwargs=kwargs))
        return ret

    return _collect
