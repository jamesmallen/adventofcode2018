import pytest

from adventofcode2018 import day06


@pytest.mark.parametrize('x,output', [
    ('''
        1, 1
        1, 6
        8, 3
        3, 4
        5, 5
        8, 9
    ''', 17),
])
def test_part1(x: str, output: int) -> None:
    assert day06.part1(x) == output


@pytest.mark.parametrize('x,threshold,output', [
    ('''
        1, 1
        1, 6
        8, 3
        3, 4
        5, 5
        8, 9
    ''', 32, 16),
])
def test_part2(x: str, threshold: int, output: int) -> None:
    assert day06.part2(x, threshold) == output
