import pytest
from collections import defaultdict

from breaking_changes import collector

# TODO: add a fixture to keep clean up the result every time


@pytest.fixture(autouse=True)
def reset_result():
    collector.result = defaultdict(list)


def test_collector_decorator(reset_result):
    @collector.collect
    def func():
        return 100

    assert func() == 100
    assert dict(collector.result) == {'tests.test_collector.func':
                                      [collector.Trace(ret=100, args=tuple(), kwargs={})]}
