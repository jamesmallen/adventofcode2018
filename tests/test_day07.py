import pytest

from adventofcode2018 import day07


@pytest.mark.parametrize('x,output', [
    ('''
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
    ''', 'CABDFE'),
])
def test_part1(x: str, output: str) -> None:
    assert day07.part1(x) == output


@pytest.mark.parametrize('x,number_of_workers,base_ticks,output', [
    ('''
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
    ''', 2, 0, 15),
])
def test_part2(x: str, number_of_workers: int, base_ticks: int, output: int) -> None:
    assert day07.part2(x, number_of_workers, base_ticks) == output
