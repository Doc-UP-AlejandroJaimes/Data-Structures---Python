"""
Test cases of Big O(n^2) exercise
"""
import unittest
from io import StringIO
import sys
import pathlib
import random as rand

# Adjust the import path to include the parent directory
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from SC03_big_On_n import bubble_sort

class BigOn2Functions(unittest.TestCase):
    
    def test_bubble_sort(self):
        array = [5,4,3,2,1]
        answer = [1,2,3,4,5]
        # check test
        self.assertEqual(bubble_sort(array),array)
    
    def test_bubble_sort2(self):
        rand.seed(158478)
        array = [rand.randint(1, 10) for _ in range(10)]
        answer = sorted(array)
        # check test
        self.assertEqual(bubble_sort(array), answer)

if __name__ == "__main__":
    unittest.main()