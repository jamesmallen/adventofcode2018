from pathlib import Path
from typing import Tuple


WIDTH = 300
HEIGHT = 300


class Grid:
    def __init__(self, serial_number: int) -> None:
        self.serial_number = serial_number
        self.power_levels = {}
        self.calculate_power_levels()

    def calculate_power_levels(self) -> None:
        for x in range(1, WIDTH + 1):
            for y in range(1, HEIGHT + 1):
                self.power_levels[x, y] = self._power_level_for_cell(x, y)

    def power_for_square(self, start_x: int, start_y: int, grid_size: int) -> int:
        power = 0
        for x in range(start_x, start_x + grid_size):
            for y in range(start_y, start_y + grid_size):
                power += self.power_levels[x, y]
        return power

    def square_with_largest_power(self, grid_size: int = 3) -> Tuple[int, int, int]:
        ret = (-1, -1, -1)  # x, y, value

        for x in range(1, WIDTH - grid_size):
            for y in range(1, HEIGHT - grid_size):
                power = self.power_for_square(x, y, grid_size)
                if power > ret[2]:
                    ret = (x, y, power)

        return ret

    def power_level_for_cell(self, x: int, y: int) -> int:
        return self.power_levels[x, y]

    def _power_level_for_cell(self, x: int, y: int) -> int:
        rack_id = x + 10
        return (((rack_id * y + self.serial_number) * rack_id) // 100) % 10 - 5


def part1(x: int):
    g = Grid(x)
    return g.square_with_largest_power()


def part2(x: int):
    g = Grid(x)
    largest_squares = {}
    for grid_size in range(1, 301):
        current = g.square_with_largest_power(grid_size=grid_size)
        current = tuple([*current, grid_size])
        largest_squares[grid_size] = current
        # if current[2] < max(largest_squares.values(), key=lambda square: square[2])[2]:
        #     break
        print(f'Largest for {grid_size}: {largest_squares[grid_size]}')
    ret = max(largest_squares.values(), key=lambda square: square[2])
    return tuple([*ret[0:2], ret[3]])


if __name__ == '__main__':
    puzzle_input = int(Path('day11.txt').read_text())
    print(part1(puzzle_input))
    print(part2(puzzle_input))
