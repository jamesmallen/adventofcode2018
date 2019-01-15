from typing import Mapping

import pytest

from adventofcode2018 import day03


@pytest.mark.parametrize('x,output', [
    ('''
    #1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2
    ''', 4),
])
def test_part1(x: str, output: int) -> None:
    assert day03.part1(x) == output


@pytest.mark.parametrize('x,output', [
    ('''
    #1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2
    ''', 3),
])
def test_part2(x: str, output: int) -> None:
    assert list(day03.part2(x))[0] == output

