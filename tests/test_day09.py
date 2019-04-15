import pytest

from adventofcode2018 import day09


@pytest.mark.parametrize('x,output', [
    ('9 players; last marble is worth 25 points', 32),
    ('10 players; last marble is worth 1618 points', 8317),
    ('13 players; last marble is worth 7999 points', 146373),
    ('17 players; last marble is worth 1104 points', 2764),
    ('21 players; last marble is worth 6111 points', 54718),
    ('30 players; last marble is worth 5807 points', 37305),
])
def test_part1(x: str, output: str) -> None:
    assert day09.part1(x) == output


@pytest.mark.parametrize('x,output', [
])
def test_part2(x: str, output: int) -> None:
    assert day09.part2(x) == output
