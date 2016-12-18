import os
import pytest

from unittest import mock

from breaking_changes import inspector

from tests import mod


def relative(subpath: str) -> str:
    return os.path.join(os.path.dirname(__file__), subpath)


def func(a, b=None):
    pass


def test_argspec():
    inspector.function_args(func) == {'args': ['a', 'b'], 'keywords': None, 'defaults': (None,), 'varargs': None}


def test_get_public_interface():
    inspector.public_interface(mod) == [('public_func', mod.public_func)]


@pytest.mark.parametrize(('path', 'modules'), [
    ('tests', ['tests/test_inspector.py', 'tests/mod.py', 'tests/__init__.py', 'tests/test_collector.py'])
])
def test_iterate_modules(path, modules):
    assert sorted(inspector.iter_modules(path, skip_tests=False)) == sorted(modules)


@pytest.mark.parametrize(('inp', 'out'), [
    ('package/module.py', 'package.module'),
    ('module.py', 'module'),
])
def test_path_to_module(inp, out):
    assert inspector.path_to_module(inp) == out


@pytest.mark.parametrize(('pkg_name', 'packages'), [
    ('package1', ['a', 'b']),
    ('package2', ['a'])
])
def test_package_collection(pkg_name: str, packages: list):
    res = list(inspector.modules(relative(pkg_name)))
    assert list(inspector.modules(relative(pkg_name))) == packages
