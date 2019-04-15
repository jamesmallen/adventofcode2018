import contextlib
import re
from collections import deque
from pathlib import Path
from typing import Set, MutableSet, Iterable, MutableMapping, MutableSequence, Sequence, Tuple


class MarbleGame:
    def __init__(self, number_of_players: int, last_marble: int) -> None:
        self.number_of_players = number_of_players
        self.last_marble = last_marble
        self.complete = False
        self.scores = [0] * number_of_players
        # self.marbles = [0]
        self.marbles = deque([0])
        self.marble_index = 0
        self.player_index = 0

    @property
    def high_score(self) -> int:
        if not self.complete:
            self.play()
        return max(self.scores)

    def play(self) -> None:
        for turn in range(1, self.last_marble + 1):
            self.tick(turn)

    def tick(self, marble: int) -> None:
        if marble % 23 == 0:
            self.marbles.rotate(7)
            self.scores[self.player_index] += marble + self.marbles.pop()
            self.marbles.rotate(-1)
        else:
            self.marbles.rotate(-1)
            self.marbles.append(marble)
        self.player_index += 1
        self.player_index %= self.number_of_players


def part1(x: str) -> int:
    match = re.search(r'(?P<number_of_players>\d+) players; last marble is worth (?P<last_marble>\d+) points', x)
    game = MarbleGame(number_of_players=int(match.group('number_of_players')),
                      last_marble=int(match.group('last_marble')))
    return game.high_score


def part2(x: str) -> int:
    match = re.search(r'(?P<number_of_players>\d+) players; last marble is worth (?P<last_marble>\d+) points', x)
    game = MarbleGame(number_of_players=int(match.group('number_of_players')),
                      last_marble=int(match.group('last_marble')) * 100)
    return game.high_score


if __name__ == '__main__':
    puzzle_input = Path('day09.txt').read_text()
    print(part1(puzzle_input))
    print(part2(puzzle_input))
