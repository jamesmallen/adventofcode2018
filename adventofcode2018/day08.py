import contextlib
import re
from pathlib import Path
from typing import Set, MutableSet, Iterable, MutableMapping, MutableSequence, Sequence, Tuple


class Node:
    def __init__(self):
        self.children: MutableSequence[Node] = []
        self.metadata: MutableSequence[int] = []


def parse_nodes(numbers: Sequence[int]) -> Tuple[Node, int]:
    node = Node()
    number_of_children = numbers[0]
    number_of_metadata = numbers[1]
    offset = 2
    for _ in range(number_of_children):
        child, chopped = parse_nodes(numbers[offset:])
        node.children.append(child)
        offset += chopped
    for i in range(offset, offset + number_of_metadata):
        node.metadata.append(numbers[i])
    return node, offset + number_of_metadata


def sum_metadata(root: Node) -> int:
    return sum(root.metadata) + sum(sum_metadata(child) for child in root.children)


def value_of_node(root: Node) -> int:
    if not root.children:
        return sum(root.metadata)
    ret = 0
    for index in root.metadata:
        if index == 0:
            # skip 0
            continue
        with contextlib.suppress(IndexError):
            # skip missing nodes
            ret += value_of_node(root.children[index - 1])
    return ret


def part1(x: str) -> int:
    root, _ = parse_nodes([int(y) for y in x.split()])
    return sum_metadata(root)


def part2(x: str) -> int:
    root, _ = parse_nodes([int(y) for y in x.split()])
    return value_of_node(root)


if __name__ == '__main__':
    puzzle_input = Path('day08.txt').read_text()
    print(part1(puzzle_input))
    print(part2(puzzle_input))
