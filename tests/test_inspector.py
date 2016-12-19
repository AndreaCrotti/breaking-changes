import os
import pytest

from unittest import mock

from breaking_changes import inspector

from tests import mod

TEST_ROOT = os.path.dirname(__file__)
BASE_ROOT = os.path.abspath(os.path.join(TEST_ROOT, '..'))


def relative(subpath: str) -> str:
    return os.path.abspath(os.path.join(TEST_ROOT, subpath))


def func(a, b=None):
    pass


def test_argspec():
    inspector.function_args(func) == {'args': ['a', 'b'], 'keywords': None, 'defaults': (None,), 'varargs': None}


def test_list_functions():
    assert list(inspector.functions(relative('package1/a.py'), BASE_ROOT)) == ['func1', 'func2']


def test_get_public_interface():
    inspector.public_interface(mod) == [('public_func', mod.public_func)]


@pytest.mark.parametrize(('pkg_name', 'packages'), [
    ('package1', ['a', 'b']),
    ('package2', ['a', 'nested.c'])
])
def test_package_collection(pkg_name: str, packages: list):
    assert list(inspector.modules(relative(pkg_name), skip_tests=False)) == packages


@pytest.mark.parametrize(('full', 'base', 'module'), [
    ('/some/long/path/to/module.py', '/some/long/path/to', 'module'),
    ('/some/long/path/to/module.py', '/some/long/path', 'to.module'),
])
def test_module_transformation(full, base, module):
    assert inspector.module_transform(full, base) == module
