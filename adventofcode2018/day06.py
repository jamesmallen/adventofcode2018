import collections
import re
from pathlib import Path
from typing import Tuple, Mapping, MutableMapping, Sequence, Set

import colored

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


class Grid:
    def __init__(self, puzzle_input: str = '') -> None:
        self.coordinates: MutableMapping[Tuple[int, int], Coordinate] = {}
        self.next_char = 'A'
        self.dirty = True
        self._closeness_grid = None
        for match in re.finditer(r'(?P<x>\d+), (?P<y>\d+)', puzzle_input):
            self.add_coordinate(int(match.group('x')), int(match.group('y')))

    def add_coordinate(self, x: int, y: int) -> None:
        self.coordinates[x, y] = Coordinate(x, y, grid=self, char=self.next_char)
        self.next_char = chr(ord(self.next_char) + 1)
        self.dirty = True

    def closest_coordinates(self, x: int, y: int) -> Sequence['Coordinate']:
        closest_coordinates = []
        closest_distance = float('inf')
        for coordinate in self.coordinates.values():
            distance = coordinate.distance_to(x, y)
            if not closest_coordinates or distance < closest_distance:
                closest_coordinates = [coordinate]
                closest_distance = distance
            elif distance == closest_distance:
                closest_coordinates.append(coordinate)
        return closest_coordinates

    @property
    def bounds(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Returns bounds as a 2-tuple of (x, y), (x, y)
        """
        return (
            (min(x for x, y in self.coordinates), min(y for x, y in self.coordinates)),
            (max(x for x, y in self.coordinates), max(y for x, y in self.coordinates)),
        )

    @property
    def closeness_grid(self) -> MutableMapping[Tuple[int, int], 'Coordinate']:
        if self.dirty:
            cg = {}
            bounds = self.bounds

            for y in range(bounds[0][1] - 1, bounds[1][1] + 2):
                for x in range(bounds[0][0] - 1, bounds[1][0] + 2):
                    if (x, y) in self.coordinates:
                        cg[x, y] = self.coordinates[x, y]
                    else:
                        closest = self.closest_coordinates(x, y)
                        if len(closest) == 1:
                            cg[x, y] = closest[0]
                        else:
                            cg[x, y] = None
            self._closeness_grid = cg
            self.dirty = False
        return self._closeness_grid

    def __str__(self):
        bounds = self.bounds
        ret = ''
        for y in range(bounds[0][1] - 1, bounds[1][1] + 2):
            for x in range(bounds[0][0] - 1, bounds[1][0] + 2):
                coord = self.closeness_grid[x, y]
                if coord is None:
                    ret += ' '
                elif coord.x == x and coord.y == y:
                    ret += colored.stylize(coord.char, colored.attr('underlined'))
                else:
                    ret += coord.char
            ret += '\n'
        return ret

    def infinite_coords(self) -> Set['Coordinate']:
        bounds = self.bounds

        ret = set()

        for x in range(bounds[0][0], bounds[1][0] + 1):
            ret.add(self.closeness_grid[x, bounds[0][1]])
            ret.add(self.closeness_grid[x, bounds[1][1]])

        for y in range(bounds[0][1], bounds[1][1] + 1):
            ret.add(self.closeness_grid[bounds[0][0], y])
            ret.add(self.closeness_grid[bounds[1][0], y])

        return ret - {None}

    def finite_areas(self) -> Mapping['Coordinate', int]:
        ignore_coords = self.infinite_coords()
        counter = collections.Counter(self.closeness_grid.values())
        return {key: value for key, value in counter.items() if key not in ignore_coords and key is not None}

    def coordinate_score(self, x: int, y: int) -> int:
        return sum(coordinate.distance_to(x, y) for coordinate in self.coordinates.values())

    def safe_area(self, threshold: int) -> int:
        bounds = self.bounds
        ret = 0

        for y in range(bounds[0][1], bounds[1][1] + 1):
            for x in range(bounds[0][0], bounds[1][0] + 1):
                if self.coordinate_score(x, y) < threshold:
                    ret += 1

        return ret


class Coordinate:
    def __init__(self, x: int, y: int, grid: Grid, char: str) -> None:
        self.x = x
        self.y = y
        self.grid = grid
        self.char = char

    def distance_to(self, x: int, y: int) -> int:
        """
        Returns the distance to a given coordinate
        """
        return abs(self.x - x) + abs(self.y - y)

    def __str__(self) -> str:
        return self.char

    def __repr__(self):
        return str(self)

    def __hash__(self) -> int:
        return ord(self.char)


def part1(x: str) -> int:
    grid = Grid(x)
    return max(grid.finite_areas().values())


def part2(x: str, threshold: int) -> int:
    grid = Grid(x)
    return grid.safe_area(threshold)


if __name__ == '__main__':
    puzzle_input = Path('day06.txt').read_text()
    print(part1(puzzle_input))
    print(part2(puzzle_input, 10000))
