import pytest

from adventofcode2018 import day01


@pytest.mark.parametrize('puzzle_input,output', [
    ('+1 -2 +3 +1', 3),
    ('+1 +1 +1', 3),
    ('+1 +1 -2', 0),
    ('-1 -2 -3', -6),
])
def test_examples(puzzle_input: str, output: int) -> None:
    assert day01.resulting_frequency(puzzle_input) == output


@pytest.mark.parametrize('x,output', [
    ('+1 -1', 0),
    ('+3 +3 +4 -2 -4', 10),
    ('-6 +3 +8 +5 -6', 5),
    ('+7 +7 -2 -7 -4', 14),
])
def test_part2_examples(x: str, output: int) -> None:
    assert day01.twice_frequency(x) == output
