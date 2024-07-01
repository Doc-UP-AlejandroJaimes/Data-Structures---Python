"""
Test cases of Big O(n) exercise
"""
import unittest
from io import StringIO
import sys
import pathlib

# Adjust the import path to include the parent directory
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from SC02_big_On import print_items

class BigOnFunctions(unittest.TestCase):
    
    def test_print_items(self):
        n = 5
        expected_output = "1\n2\n3\n4\n5\n"
        
        # Redirect stdout to capture the print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_items(n)
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check if the captured output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)
     
    def test_print_items2(self):
        n = 10
        expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
        
        # Redirect stdout to capture the print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_items(n)
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check if the captured output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)
    
if __name__ == "__main__":
    unittest.main()