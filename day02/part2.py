import os
from typing import List
from typing import Tuple
from unittest.mock import mock_open
from unittest.mock import patch

import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_inputs() -> List[Tuple[str, int]]:
    with open(os.path.join(BASE_DIR, 'input.txt')) as fp:
        inputs: List[str] = fp.read().strip().splitlines()

    movements: List[Tuple[str, int]] = []
    for instruction in inputs:
        direction, delta = instruction.split()
        movements.append((direction, int(delta)))

    return movements


def calculate(movements: List[Tuple[str, int]]) -> int:
    abscissa = 0
    ordinate = 0
    aim = 0
    for direction, delta in movements:
        if direction.lower() == 'forward':
            abscissa += delta
            ordinate += aim * delta
        elif direction.lower() == 'down':
            aim += delta
        elif direction.lower() == 'up':
            aim -= delta
        else:
            raise AssertionError(f'Invalid direction found: {direction}')

    return abscissa * ordinate


def main() -> int:
    return calculate(get_inputs())


@pytest.mark.parametrize(
    ('inputs', 'expected'),
    [
        (
            '''
            forward 5
            down 5
            forward 8
            up 3
            down 8
            forward 2
            ''',
            900,
        )
    ]
)
def test(inputs: str, expected: int) -> None:
    with patch('builtins.open', mock_open(read_data=inputs)):
        assert main() == expected


if __name__ == '__main__':
    print(main())
