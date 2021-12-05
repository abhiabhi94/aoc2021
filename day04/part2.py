import os
from typing import List
from typing import Set
from typing import Tuple
from unittest.mock import mock_open
from unittest.mock import patch

import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Board:
    def __init__(self, nums: str):
        self.nums: List[int] = [int(n) for n in nums.split()]
        self.unmarked: Set[int] = set(self.nums)
        self.size = int(len(self.nums) ** 0.5)

    @property
    def has_won(self) -> bool:
        for column in range(self.size):
            for row in range(self.size):
                if self.nums[column * self.size + row] in self.unmarked:
                    break
            else:
                return True

            for row in range(self.size):
                if self.nums[row * self.size + column] in self.unmarked:
                    break
            else:
                return True
        else:
            return False


def get_inputs() -> Tuple[List[int], List['Board']]:
    with open(os.path.join(BASE_DIR, 'input.txt')) as fp:
        inputs = fp.read()

    nums, *left_over = inputs.split('\n\n')
    numbers = [int(n) for n in nums.split(',')]

    boards = [Board(b) for b in left_over]

    return numbers, boards


def calculate(nums: List[int], boards: List['Board']) -> int:
    boards_won = set()
    last_winner = -1

    for num in nums:
        for board in boards:
            board.unmarked.discard(num)

            if board.has_won and board not in boards_won:
                boards_won.add(board)
                last_winner = sum(board.unmarked) * num

    return last_winner


def main() -> int:
    return calculate(*get_inputs())


@pytest.mark.parametrize(
    ('inputs', 'expected'),
    [
        (
            '''
            7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

            22 13 17 11  0
             8  2 23  4 24
            21  9 14 16  7
             6 10  3 18  5
             1 12 20 15 19

             3 15  0  2 22
             9 18 13 17  5
            19  8  7 25 23
            20 11 10 24  4
            14 21 16 12  6

            14 21 17 24  4
            10 16 15  9 19
            18  8 23 26 20
            22 11 13  6  5
             2  0 12  3  7
            ''',
            1924,
        )
    ]
)
def test(inputs: str, expected: int) -> None:
    with patch('builtins.open', mock_open(read_data=inputs)):
        assert main() == expected


if __name__ == '__main__':
    print(main())
