"""
Test cases of Big O(1) exercise
"""
import unittest
import sys
import pathlib

# Adjust the import path to include the parent directory
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from SC04_big_O1_test import search_element_by_index

class BigO1Functions(unittest.TestCase):
    
    def test_found_value(self):
        array = [5,4,3,2,1,78,74]
        value = 78
        expected_index = 5
        # check test
        self.assertEqual(search_element_by_index(array, value), expected_index)
    
    def test_not_found_value(self):
        array = [55,47,33,245,10,478,754]
        value = 753
        # check test
        with self.assertRaises(ValueError):
            search_element_by_index(array, value)

if __name__ == "__main__":
    unittest.main()