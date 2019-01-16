import re
from pathlib import Path
from typing import Set, MutableSet, Iterable, MutableMapping


class Step:
    ticks_to_complete: int

    def __init__(self, char: str, base_ticks: int = 0) -> None:
        self.char = char
        self.dependencies: MutableSet[Step] = set()
        self.base_ticks = base_ticks

        self.reset()

    @property
    def is_complete(self) -> bool:
        return self.ticks_to_complete <= 0

    @property
    def is_ready(self) -> bool:
        return all(step.is_complete for step in self.dependencies)

    def depends_on(self, step: 'Step') -> None:
        self.dependencies.add(step)

    def work_on(self) -> bool:
        """
        Returns True if this work caused the step to be completed
        """
        self.ticks_to_complete -= 1
        return self.ticks_to_complete <= 0

    def complete(self) -> None:
        self.ticks_to_complete = 0

    def reset(self) -> None:
        self.ticks_to_complete = ord(self.char) - ord('A') + 1 + self.base_ticks

    def __hash__(self) -> int:
        return ord(self.char)


class DependencyGraph:
    def __init__(self, puzzle_input: str, base_ticks: int = 0) -> None:
        self.steps = {}
        self.base_ticks = base_ticks
        for match in re.finditer(r'Step (?P<depends_on>\w+) must be finished before step (?P<char>\w+) can begin.', puzzle_input):
            self.add_information(char=match.group('char'), depends_on=match.group('depends_on'))

    def add_information(self, char: str, depends_on: str) -> None:
        self.steps.setdefault(char, Step(char, base_ticks=self.base_ticks)).depends_on(
            self.steps.setdefault(depends_on, Step(depends_on, base_ticks=self.base_ticks))
        )

    def reset(self) -> None:
        for step in self.steps.values():
            step.reset()

    def incomplete_steps(self) -> Set[Step]:
        return {step for step in self.steps.values() if not step.is_complete}

    def ready_steps(self) -> Set[Step]:
        return {step for step in self.incomplete_steps() if step.is_ready}

    def next_steps(self) -> Iterable[Step]:
        yield from sorted(self.ready_steps(), key=lambda step: step.char)

    def determine_order(self) -> Iterable[Step]:
        while self.incomplete_steps():
            next_step = list(self.next_steps())[0]
            next_step.complete()
            yield next_step

    def order(self) -> str:
        return ''.join(step.char for step in self.determine_order())


class WorkGroup:
    def __init__(self, puzzle_input: str, number_of_workers: int = 2, base_ticks: int = 0) -> None:
        self.dg = DependencyGraph(puzzle_input, base_ticks=base_ticks)
        self.number_of_workers = number_of_workers
        self.workers: MutableMapping[int, Step] = {
            worker_id: None for worker_id in range(1, self.number_of_workers + 1)
        }
        self.completed = ''

    def ready_workers(self) -> Iterable[int]:
        yield from [worker_id for worker_id, step in self.workers.items() if step is None or step.is_complete]

    def steps_backlog(self) -> Iterable[Step]:
        yield from (step for step in self.dg.ready_steps() if step not in self.workers.values())

    def work(self) -> int:
        ticks = 0
        while self.dg.incomplete_steps():
            for worker_id, step in self.workers.items():
                if step and step.is_complete:
                    self.workers[worker_id] = None
            for worker_id, step in zip(self.ready_workers(), self.steps_backlog()):
                # print(f'Assigning {step.char} to {worker_id}')
                self.workers[worker_id] = step
            self.print_line(ticks)
            for step in self.workers.values():
                if step is None:
                    continue
                result = step.work_on()
                if result:
                    self.completed += step.char
            ticks += 1
        self.print_line(ticks)
        return ticks

    def print_line(self, ticks: int) -> None:
        print(f'{ticks}\t', end='')
        for step in self.workers.values():
            if step is None:
                print('.', end='')
            else:
                print(step.char, end='')
            print('\t', end='')
        print(self.completed)




def part1(x: str) -> str:
    dg = DependencyGraph(x)
    return dg.order()


def part2(x: str, number_of_workers: int, base_ticks: int) -> int:
    wg = WorkGroup(x, number_of_workers=number_of_workers, base_ticks=base_ticks)
    return wg.work()


if __name__ == '__main__':
    puzzle_input = Path('day07.txt').read_text()
    print(part1(puzzle_input))
    print(part2(puzzle_input, number_of_workers=5, base_ticks=60))
