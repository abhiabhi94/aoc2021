import os
from collections import Counter
from collections import defaultdict
from typing import Dict
from typing import List
from unittest.mock import mock_open
from unittest.mock import patch

import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_inputs() -> List[str]:
    with open(os.path.join(BASE_DIR, 'input.txt')) as fp:
        inputs = fp.read().strip().splitlines()
    return [i.strip() for i in inputs]


def calculate(nums: List[str]) -> int:
    length = len(nums[0])
    gamma: Dict[int, List[str]] = defaultdict(list)
    for num in nums:
        for index, bit in enumerate(num):
            gamma[index].append(bit)
    gamma_rates = ''
    for index in gamma:
        gamma_rates += Counter(gamma[index]).most_common(1)[0][0]

    gamma_rate = int(gamma_rates, 2)
    epsilon_rate = 2 ** length - gamma_rate - 1
    return epsilon_rate * gamma_rate


def main() -> int:
    return calculate(get_inputs())


@pytest.mark.parametrize(
    ('inputs', 'expected'),
    [
        (
            '''
            00100
            11110
            10110
            10111
            10101
            01111
            00111
            11100
            10000
            11001
            00010
            01010
            ''',
            198,
        )
    ]
)
def test(inputs: str, expected: int) -> None:
    with patch('builtins.open', mock_open(read_data=inputs)):
        assert main() == expected


if __name__ == '__main__':
    print(main())
