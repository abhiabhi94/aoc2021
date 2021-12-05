import os
from collections import defaultdict
from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Tuple
from unittest.mock import mock_open
from unittest.mock import patch

import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Point(NamedTuple):
    x: int
    y: int


class Line(NamedTuple):
    start: Point
    end: Point


def get_inputs() -> List['Line']:
    with open(os.path.join(BASE_DIR, 'input.txt')) as fp:
        inputs: List[str] = fp.read().strip().splitlines()

    lines: List['Line'] = []
    for points in inputs:
        start, end = points.strip().split('->')
        starting_point = Point(*[int(p) for p in start.strip().split(',')])
        ending_point = Point(*[int(p) for p in end.strip().split(',')])

        lines.append(Line(starting_point, ending_point))

    return lines


def calculate(lines: List['Line']) -> int:
    points_covered: Dict[Tuple[int, int], int] = defaultdict(lambda: 0)
    for line in lines:
        x_start = line.start.x
        x_end = line.end.x
        y_start = line.start.y
        y_end = line.end.y
        if x_start == x_end:
            y_min = min(line.start.y, line.end.y)
            y_max = max(line.start.y, line.end.y)
            for diff in range(y_min, y_max + 1):
                point = (x_start, diff)
                points_covered[point] += 1

        elif y_start == y_end:
            x_min = min(x_start, x_end)
            x_max = max(x_start, x_end)
            for diff in range(x_min, x_max + 1):
                point = (diff, y_start)
                points_covered[point] += 1

    dangerous_points = 0
    for value in points_covered.values():
        if value > 1:
            dangerous_points += 1

    return dangerous_points


def main() -> int:
    return calculate(get_inputs())


@pytest.mark.parametrize(
    ('inputs', 'expected'),
    [
        (
            '''
            0,9 -> 5,9
            8,0 -> 0,8
            9,4 -> 3,4
            2,2 -> 2,1
            7,0 -> 7,4
            6,4 -> 2,0
            0,9 -> 2,9
            3,4 -> 1,4
            0,0 -> 8,8
            5,5 -> 8,2
            ''',
            5,
        )
    ]
)
def test(inputs: str, expected: int) -> None:
    with patch('builtins.open', mock_open(read_data=inputs)):
        assert main() == expected


if __name__ == '__main__':
    print(main())
