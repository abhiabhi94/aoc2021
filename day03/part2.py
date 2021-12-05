import os
from collections import Counter
from typing import List
from unittest.mock import mock_open
from unittest.mock import patch

import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_inputs() -> List[str]:
    with open(os.path.join(BASE_DIR, 'input.txt')) as fp:
        inputs = fp.read().strip().splitlines()
    return [i.strip() for i in inputs]


def get_all_bits_at_nth_index(nums: List[str], index: int) -> str:
    all_bits = ''
    for num in nums:
        all_bits += num[index]
    return all_bits


def most_common_nth_bit(values: List[str], index: int) -> str:
    all_bits = get_all_bits_at_nth_index(values, index)
    common_bits = Counter(all_bits).most_common(2)
    if common_bits[0][1] == common_bits[1][1]:
        return '1'
    return common_bits[0][0]


def get_o2_rate(nums: List[str]) -> int:
    index = 0
    while(len(nums) > 1 or index < len(nums)):
        most_common_bit = most_common_nth_bit(nums, index)
        nums = list(filter(lambda b: b[index] == most_common_bit, nums))
        index += 1

    return int(nums[0], 2)


def get_co2_rate(nums: List[str]) -> int:
    index = 0
    while(len(nums) > 1 or index < len(nums)):
        most_common_bit = most_common_nth_bit(nums, index)

        if most_common_bit == '0':
            least_common_bit = '1'
        else:
            least_common_bit = '0'

        nums = list(filter(lambda b: b[index] == least_common_bit, nums))
        index += 1

    return int(nums[0], 2)


def calculate(nums: List[str]) -> int:
    return get_co2_rate(nums) * get_o2_rate(nums)


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
            230,
        )
    ]
)
def test(inputs: str, expected: int) -> None:
    with patch('builtins.open', mock_open(read_data=inputs)):
        assert main() == expected


if __name__ == '__main__':
    print(main())
