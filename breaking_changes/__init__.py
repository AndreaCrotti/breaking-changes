import inspect
import re
import scandir

from os import path

PY_FILE_REGEXP = re.compile(r'[a-z_]\w*.py$')


def function_args(func):
    args = inspect.getargspec(func)
    return dict(args._asdict())


def _is_public_function(func):
    return inspect.isfunction(func) and not func.__name__.startswith('_')


def public_interface(module):
    return inspect.getmembers(module, predicate=_is_public_function)


def iter_modules(pth):
    for root, dirs, files in scandir.walk(pth):
        py_files = filter(lambda v: PY_FILE_REGEXP.match(v), files)
        for py in py_files:
            yield path.join(root, py)
