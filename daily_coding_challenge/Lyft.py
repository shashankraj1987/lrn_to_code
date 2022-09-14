from typing import List
import numpy as np


def sum_9(input_lst: List[int]) -> List[int]:
    """
    This problem was asked by Lyft.
    Given a list of integers and a number K, return which contiguous elements of the list sum to K.
    For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
    """
    # TODO: Works but messy. Make it better

    lst = []
    if len(input_lst) < 1:
        return [-1]
    elif len(input_lst) == 1 & input_lst[0] != 9:
        return [-1]
    elif len(input_lst) == 1 & input_lst[0] == 9:
        return input_lst
    else:
        for i in input_lst:
            if np.sum(lst) < 9:
                lst.append(i)
            elif np.sum(lst) == 9:
                return lst

        if np.sum(lst) != 9:
            lst = []
            while np.sum(lst) < 9:
                lst.append(input_lst.pop())

        if np.sum(lst) == 9:
            return lst
        else:
            return [-1]


if __name__ == '__main__':
    print(sum_9([1, 1, 3, 5]))
    print(len([]))
    print(sum_9([0, 0, 0, 9]))
