import pytest

from adventofcode2018 import day11


@pytest.mark.parametrize('x,y,serial_number,output', [
    (3, 5, 8, 4),
    (122, 79, 57, -5),
    (217, 196, 39, 0),
    (101, 153, 71, 4),
])
def test_power_level_of_cell(x: int, y: int, serial_number: int, output: int) -> None:
    assert day11.Grid(serial_number).power_level_for_cell(x, y) == output


@pytest.mark.parametrize('serial_number,output_x,output_y', [
    (18, 33, 45),
    (42, 21, 61),
])
def test_part1(serial_number: int, output_x: int, output_y: int) -> None:
    assert day11.part1(serial_number)[:2] == (output_x, output_y)

@pytest.mark.parametrize('serial_number,output_x,output_y,output_size', [
    (18, 90, 269, 16),
    (42, 232, 251, 12),
])
def test_part2(serial_number: int, output_x: int, output_y: int, output_size) -> None:
    assert day11.part2(serial_number) == (output_x, output_y, output_size)

#
#
# @pytest.mark.parametrize('x,output', [
# ])
# def test_part2(x: str, output: int) -> None:
#     assert day09.part2(x) == output
