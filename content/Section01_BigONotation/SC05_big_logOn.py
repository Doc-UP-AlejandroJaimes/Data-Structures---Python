"""
Represents concept Big Log O(n)

Example: Binary search.
"""
from typing import Union
import numpy as np

def binary_search(sort_array:np.ndarray, value:int) -> Union[int, int]:
    left, right = 0, len(sort_array) - 1
    index = -1
    iterations = 0
    while left < right:
        # calculate middle index
        middle_index = (left + right) // 2
        # compare
        if value == sort_array[middle_index]:
            index = middle_index
            break
        if value > sort_array[middle_index]:
            left = middle_index + 1
        if value < sort_array[middle_index]:
            right = middle_index - 1
        iterations += 1
    return index, iterations

if __name__ == "__main__":
    # sort array ascending
    array = np.arange(1, 1001)
    print(type(array))
    # search element
    value = 52
    index_searched, iterations = binary_search(array, value)
    # output
    print(f"Sorted Array: {array}\nIndex Searched: {index_searched}\n# Iterations: {(iterations + 1)}")