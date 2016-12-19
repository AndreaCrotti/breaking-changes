import glob
import importlib
import inspect
import logging
import re
import scandir
import pathlib

import click

from collections import defaultdict
from os import path
from typing import Callable, Generator

logger = logging.getLogger(__name__)


PY_FILE_REGEXP = re.compile(r'[a-z_]\w*.py$')
PY_FILE_PUBLIC = re.compile(r'[a-z]\w*.py$') # only "public modules" here


def function_args(func: Callable) -> dict:
    args = inspect.getargspec(func)
    return dict(args._asdict())


def _is_public_function(func: Callable) -> bool:
    return inspect.isfunction(func) and not func.__name__.startswith('_')


def public_interface(module):
    return inspect.getmembers(module, predicate=_is_public_function)


def module_transform(full: str, root: str) -> str:
    rel = pathlib.Path(full).relative_to(root)
    return str(rel).replace('/', '.')[:-3]


def modules(pth: str, skip_tests: bool=True) -> Generator:
    for root, dirs, files in scandir.walk(pth):
        if not skip_tests or 'tests' not in root:
            py_files = filter(lambda v: PY_FILE_PUBLIC.match(v), files)
            for py in py_files:
                print(path.join(root, py))
                yield module_transform(path.join(root, py), pth)


def functions(mod_path: str, root: str) -> Generator:
    mod = module_transform(mod_path, root)
    mod_obj = importlib.import_module(mod)
    return [x[0] for x in public_interface(mod_obj)]


@click.group()
@click.pass_context
def cli(ctx):
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)


@cli.command(help='report analysis')
@click.argument('path')
@click.pass_context
def report(ctx, path):
    # list of things to report that actually define a package
    # - modules
    # - functions
    # - variables
    from pprint import pprint
