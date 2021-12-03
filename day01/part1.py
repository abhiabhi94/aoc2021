import itertools
import os
from typing import List
from unittest.mock import mock_open
from unittest.mock import patch

import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_inputs() -> List[int]:
    with open(os.path.join(BASE_DIR, 'input.txt')) as fp:
        inputs = fp.read().strip().splitlines()
    return [int(n) for n in inputs]


def calculate(depths: List[int]) -> int:
    increase = 0
    length = len(depths)
    for next_depth, previous_depth in zip(
        itertools.islice(depths, 1, length),
        itertools.islice(depths, 0, length - 1)
    ):
        if next_depth - previous_depth > 0:
            increase += 1

    return increase


def main() -> int:
    return calculate(get_inputs())


@pytest.mark.parametrize(
    ('inputs', 'expected'),
    [
        (
            '''
            199
            200
            208
            210
            200
            207
            240
            269
            260
            263
            ''',
            7,
        )
    ]
)
def test(inputs: str, expected: int) -> None:
    with patch('builtins.open', mock_open(read_data=inputs)):
        assert main() == expected


if __name__ == '__main__':
    print(main())
