import pytest

from adventofcode2018 import day08


@pytest.mark.parametrize('x,output', [
    ('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2', 138),
])
def test_part1(x: str, output: str) -> None:
    assert day08.part1(x) == output


@pytest.mark.parametrize('x,output', [
    ('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2', 66),
])
def test_part2(x: str, output: int) -> None:
    assert day08.part2(x) == output
