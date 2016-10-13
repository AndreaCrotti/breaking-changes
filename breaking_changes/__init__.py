import argparse
import importlib
import inspect
import re
import scandir

from collections import defaultdict
from os import path

PY_FILE_REGEXP = re.compile(r'[a-z_]\w*.py$')


def function_args(func):
    args = inspect.getargspec(func)
    return dict(args._asdict())


def path_to_module(path):
    return path.replace('/', '.')[:-3]


def _is_public_function(func):
    return inspect.isfunction(func) and not func.__name__.startswith('_')


def public_interface(module):
    return inspect.getmembers(module, predicate=_is_public_function)


def iter_modules(pth):
    for root, dirs, files in scandir.walk(pth):
        py_files = filter(lambda v: PY_FILE_REGEXP.match(v), files)
        for py in py_files:
            yield path.join(root, py)


def analyze(root):
    result = defaultdict(dict)
    for mod_path in iter_modules(root):
        mod = path_to_module(mod_path)
        mod_obj = importlib.import_module(mod)

        for func_name, func in public_interface(mod_obj):
            result[mod][func_name] = function_args(func)

    return result


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze signatures')

    parser.add_argument('-p', '--path',
                        required=True,
                        help='path to analyze')

    return parser.parse_args()


def main():
    args = parse_arguments()
    from pprint import pprint
    pprint(dict(analyze(root=args.path)))
