import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import MutableSequence, Tuple


@dataclass
class PointOfLight:
    position: Tuple[int, int]
    velocity: Tuple[int, int]

    def tick(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )


class Sky:
    def __init__(self):
        self.points: MutableSequence[PointOfLight] = []
        self.time = 0

    def add_point(self, position: Tuple[int, int], velocity: Tuple[int, int]) -> None:
        self.points.append(PointOfLight(position=position, velocity=velocity))

    def tick(self):
        for point in self.points:
            point.tick()
        self.time += 1

    def bounds(self):
        return (
            (min(point.position[0] for point in self.points), min(point.position[1] for point in self.points)),
            (max(point.position[0] for point in self.points), max(point.position[1] for point in self.points)),
        )

    def map(self):
        ret = ''
        bounds = self.bounds()
        screen = defaultdict(lambda: '.')
        for point in self.points:
            screen[point.position[0], point.position[1]] = '#'

        for y in range(bounds[0][1], bounds[1][1] + 1):
            for x in range(bounds[0][0], bounds[1][0] + 1):
                ret += screen[x, y]
            ret += '\n'
        return ret

    def __str__(self):
        return self.map()


def part1(x: str):
    sky = Sky()
    for match in re.finditer(r'position=<\s*(?P<pos_x>[\d-]+),\s*(?P<pos_y>[\d-]+)> '
                             r'velocity=<\s*(?P<vel_x>[\d-]+),\s*(?P<vel_y>[\d-]+)>',
                             x):
        position = (int(match.group('pos_x')), int(match.group('pos_y')))
        velocity = (int(match.group('vel_x')), int(match.group('vel_y')))
        sky.add_point(position, velocity)
    triggered = False

    while True:
        # wait until height is <= 10
        bounds = sky.bounds()
        if abs(bounds[1][1] - bounds[0][1]) <= 10:
            print(f'After {sky.time} seconds:')
            print(sky.map() + '\n')
            triggered = True
        elif triggered:
            break
        sky.tick()


if __name__ == '__main__':
    test_input = Path('day10_test.txt').read_text()
    part1(test_input)

    puzzle_input = Path('day10.txt').read_text()
    print(part1(puzzle_input))
