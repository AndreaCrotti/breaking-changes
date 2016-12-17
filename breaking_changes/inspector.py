import importlib
import inspect
import re
import scandir

import click

from collections import defaultdict
from os import path
from typing import Callable, Generator


PY_FILE_REGEXP = re.compile(r'[a-z_]\w*.py$')


def function_args(func: Callable) -> dict:
    args = inspect.getargspec(func)
    return dict(args._asdict())


def path_to_module(path: str) -> str:
    return path.replace('/', '.')[:-3]


def _is_public_function(func: Callable) -> bool:
    return inspect.isfunction(func) and not func.__name__.startswith('_')


def public_interface(module):
    return inspect.getmembers(module, predicate=_is_public_function)


def iter_modules(pth: str, skip_tests: bool=True) -> Generator:
    for root, dirs, files in scandir.walk(pth):
        if not skip_tests or 'tests' not in root:
            py_files = filter(lambda v: PY_FILE_REGEXP.match(v), files)
            for py in py_files:
                yield path.join(root, py)


def analyze(root: str, skip_tests: bool=True) -> defaultdict:
    result = defaultdict(dict)
    for mod_path in iter_modules(root, skip_tests=skip_tests):
        mod = path_to_module(mod_path)
        try:
            mod_obj = importlib.import_module(mod)
        except ImportError:
            print(mod_path)
            continue

        for func_name, func in public_interface(mod_obj):
            try:
                result[mod][func_name] = function_args(func)
            except ValueError:
                print(mod, func_name)

    return result


@click.group()
@click.pass_context
def cli(ctx):
    pass
