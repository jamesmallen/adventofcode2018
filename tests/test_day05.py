import pytest

from adventofcode2018 import day05


@pytest.mark.parametrize('x,output', [
    ('aA', 0),
    ('abBA', 0),
    ('abAB', 4),
    ('aabAAB', 6),
    ('dabAcCaCBAcCcaDA', 10),
])
def test_part1(x: str, output: int) -> None:
    assert day05.part1(x) == output


@pytest.mark.parametrize('x,output', [
    ('''
    ''', 4455),
])
def test_part2(x: str, output: int) -> None:
    pass

#
# @pytest.mark.parametrize('x,output', [
#     ('''
#     #1 @ 1,3: 4x4
#     #2 @ 3,1: 4x4
#     #3 @ 5,5: 2x2
#     ''', 3),
# ])
# def test_part2(x: str, output: int) -> None:
#     assert day03.part2(x) == output
#
