from typing import Mapping

import pytest

from adventofcode2018 import day02


@pytest.mark.parametrize('x,output', [
    ('abcdef', {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}),
    ('bababc', {'a': 2, 'b': 3, 'c': 1}),
    ('abbcde', {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 1}),
    ('abcccd', {'a': 1, 'b': 1, 'c': 3, 'd': 1}),
    ('aabcdd', {'a': 2, 'b': 1, 'c': 1, 'd': 2}),
    ('abcdee', {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2}),
    ('ababab', {'a': 3, 'b': 3}),
])
def test_letter_count(x: str, output: Mapping[str, int]) -> None:
    assert day02.letter_count(x) == output


@pytest.mark.parametrize('x,output', [
    ('abcdef bababc abbcde abcccd aabcdd abcdee ababab', 12),
])
def test_part1(x: str, output: int) -> None:
    assert day02.part1(x) == output


@pytest.mark.parametrize('x,y,output', [
    ('fghij', 'fguij', 'fgij'),
])
def test_str_common(x: str, y: str, output: str) -> None:
    assert day02.str_common(x, y) == output


@pytest.mark.parametrize('x,output', [
    ('abcde fghij klmno pqrst fguij axcye wvxyz', 'fgij'),
])
def test_part2(x: str, output: int) -> None:
    assert day02.part2(x) == output

