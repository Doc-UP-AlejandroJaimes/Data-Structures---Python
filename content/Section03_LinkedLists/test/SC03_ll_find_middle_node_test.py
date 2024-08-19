import unittest
import sys
import pathlib

# Adjust the import path to include the parent directory
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from exercises.SC03_ll_find_middle_node import LinkedList

class TestLinkedList(unittest.TestCase):
    """
    Test cases for the LinkedList class, focusing on the find_middle_node method.
    """
    
    def test_even_number_of_nodes(self):
        """
        Test that the middle node is correctly identified in a list with an even number of nodes.
        The expected middle node for [1, 2, 3, 4] is 3.
        """
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        expected_middle = 3
        actual_middle = my_linked_list.find_middle_node().value
        self.assertEqual(
            actual_middle, 
            expected_middle, 
            f"Failed: Expected middle node value to be {expected_middle}, but got {actual_middle}."
        )
        
    def test_odd_number_of_nodes(self):
        """
        Test that the middle node is correctly identified in a list with an odd number of nodes.
        The expected middle node for [1, 2, 3, 4, 5] is 3.
        """
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        expected_middle = 3
        actual_middle = my_linked_list.find_middle_node().value
        self.assertEqual(
            actual_middle, 
            expected_middle, 
            f"Failed: Expected middle node value to be {expected_middle}, but got {actual_middle}."
        )
        
    def test_single_node(self):
        """
        Test that the middle node is correctly identified in a list with a single node.
        The expected middle node for [1] is 1.
        """
        my_linked_list = LinkedList(1)
        expected_middle = 1
        actual_middle = my_linked_list.find_middle_node().value
        self.assertEqual(
            actual_middle, 
            expected_middle, 
            f"Failed: Expected middle node value to be {expected_middle}, but got {actual_middle}."
        )
        
if __name__ == "__main__":
    unittest.main()
