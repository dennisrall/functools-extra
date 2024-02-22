import pytest

from functools_extra import pipe


def add_one(x: int) -> int:
    return x + 1


@pytest.mark.parametrize("num_funcs", range(9))
def test_pipe(num_funcs):
    assert pipe(0, *([add_one] * num_funcs)) == num_funcs
