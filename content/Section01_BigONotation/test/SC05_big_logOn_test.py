"""
Test cases of Big Log O(n) exercise
"""
import unittest
import sys
import pathlib
import numpy as np

# Adjust the import path to include the parent directory
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from SC05_big_logOn import binary_search

class BigLogOnFunctions(unittest.TestCase):
    
    def binary_search_1Kelements(self):
        arr = np.arange(1, 1001)
        value = 580
        expected_index = 579
        index, iterations = binary_search(arr, value)
        # check test
        self.assertEqual(index, expected_index)
        self.assertLessEqual(iterations, int(np.log2(len(arr)) + 1))

    def binary_search_5Kelements(self):
        arr = np.arange(1, 5001)
        value = 4096
        expected_index = 4095
        index, iterations = binary_search(arr, value)
        # check test
        self.assertEqual(index, expected_index)
        self.assertLessEqual(iterations, int(np.log2(len(arr)) + 1))
    
    def binary_search_not_found_value(self):
        array = np.arange(1, 1001)
        value = 1001
        expected_index = -1
        index, iterations = binary_search(array, value)
        self.assertEqual(index, expected_index)
        self.assertLessEqual(iterations, int(np.log2(len(array)) + 1))

if __name__ == "__main__":
    unittest.main()