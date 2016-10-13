import pytest

try:
    from unittest import mock
except ImportError:
    import mock

import breaking_changes

from tests import mod


def func(a, b=None):
    pass


def test_argspec():
    breaking_changes.function_args(func) == {'args': ['a', 'b'], 'keywords': None, 'defaults': (None,), 'varargs': None}


def test_get_public_interface():
    breaking_changes.public_interface(mod) == [('public_func', mod.public_func)]


@pytest.mark.parametrize(('path', 'modules'), [
    ('tests', ['tests/test_changes.py', 'tests/mod.py', 'tests/__init__.py'])
])
def test_iterate_modules(path, modules):
    assert sorted(breaking_changes.iter_modules(path)) == sorted(modules)


@pytest.mark.parametrize(('inp', 'out'), [
    ('package/module.py', 'package.module'),
    ('module.py', 'module'),
])
def test_path_to_module(inp, out):
    assert breaking_changes.path_to_module(inp) == out
