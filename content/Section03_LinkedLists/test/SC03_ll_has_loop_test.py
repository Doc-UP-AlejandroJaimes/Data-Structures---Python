import unittest
import sys
import pathlib

# Adjust the import path to include the parent directory
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from exercises.SC03_ll_has_loop import LinkedList

class TestLinkedList(unittest.TestCase):
    """
    Test cases for the LinkedList class, focusing on the has_loop method.
    """
    
    def test_has_no_loop(self):
        """
        Test that the has_loop method correctly identifies a linked list with no loop.
        A list with nodes [1, 2, 3, 4, 4, 4, 7, 8] should return False as it has no cycle.
        """
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(4)
        my_linked_list.append(4)
        my_linked_list.append(7)
        my_linked_list.append(8)
        expected_output = False
        actual_output = my_linked_list.has_loop()
        self.assertEqual(
            actual_output, 
            expected_output, 
            f"Failed: Expected output to be {expected_output}, but got {actual_output}."
        )
        
    def test_has_loop(self):
        """
        Test that the has_loop method correctly identifies a linked list with a loop.
        A list with nodes [1, 2, 3, 4] where the last node points back to the head should return True.
        """
        my_linked_list_1 = LinkedList(1)
        my_linked_list_1.append(2)
        my_linked_list_1.append(3)
        my_linked_list_1.append(4)
        my_linked_list_1.tail.next = my_linked_list_1.head
        expected_output = True
        actual_output = my_linked_list_1.has_loop()
        self.assertEqual(
            actual_output, 
            expected_output, 
            f"Failed: Expected output to be {expected_output}, but got {actual_output}."
        )
        
    def test_single_node(self):
        """
        Test that the has_loop method correctly identifies that a single-node linked list has no loop.
        A list with a single node [1] should return False as it cannot form a cycle.
        """
        my_linked_list = LinkedList(1)
        expected_output = False
        actual_output = my_linked_list.has_loop()
        self.assertEqual(
            actual_output, 
            expected_output, 
            f"Failed: Expected output value to be {expected_output}, but got {actual_output}."
        )
        
if __name__ == "__main__":
    unittest.main()
