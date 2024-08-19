"""LL: Find Middle Node ( ** Interview Question)

Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

1. The method should use a two-pointer approach, 
   where one pointer (slow) moves one node at a time 
   and the other pointer (fast) moves two nodes at a time.

2. When the fast pointer reaches the end of the list or has no next node,
   the slow pointer should be at the middle node of the list.

3. The method should return the middle node when the number 
   of nodes is odd or the first node of the second half of 
   the list if the list has an even number of nodes.

4. The method should only traverse the linked list once.
   In other words, you can only use one loop.

"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = (new_node, new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self) -> Node:
        if self.head.next is None:
            return self.head
        # establsh pointers
        slow = self.head
        fast = self.head.next
        find_node = None
        counter = 0
        while fast.next is not None:
            find_node = slow
            fast = fast.next
            slow = slow.next
            counter += 1
        return find_node.next if counter % 2 == 0 else find_node
    
    def print_list(self) -> None:
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end=" ")
            tmp = tmp.next