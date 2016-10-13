import inspect


def function_args(func):
    args = inspect.getargspec(func)
    return dict(args._asdict())


def _is_public_function(func):
    return inspect.isfunction(func) and not func.__name__.startswith('_')


def public_interface(module):
    return inspect.getmembers(module, predicate=_is_public_function)
