"""Python Linked List

Methods

---- LINKED LIST ---

Append    O(1)
Pop       O(n)
Prepend   O(1)
Pop First O(1)
Insert    O(n)
Remove    O(n)
Lookup By Index O(n)
Lookup By Value O(n)

---- LIST ---

Append    O(1)
Pop       O(1)
Prepend   O(n)
Pop First O(n)
Insert    O(n)
Remove    O(n)
Lookup By Index O(1)
Lookup By Value O(n)

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
        self.length = 1

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = (new_node, new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        tmp = self.head
        pre = self.head
        while (tmp.next):
            pre = tmp
            tmp = tmp.next
        # update values
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # check single value
        if self.length == 0:
            self.head, self.tail = (None, None)
        return tmp
        
    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:   
            current_head = self.head
            self.head = new_node
            self.head.next = current_head
        self.length += 1
        return True
        
    def pop_first(self):
        if self.length == 0:
            return None
        first_element = self.head
        self.head = self.head.next
        first_element.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return first_element
    
    def get(self, index) -> Node:
        # check that is on the limits
        if index < 0 or index >= self.length:
            return None
        #check if the node seaking is the first
        if index == 0:
            return self.head
        # check if the node seaking is the last
        if index == self.length - 1:
            return self.tail
        # otherwise iterate
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp
    
    def set_value(self, index, value) -> bool:
        # search and update node
        node_searched = self.get(index)
        # check that is on the limits
        if not node_searched:
            return False
        node_searched.value = value
        return True
    
    def insert(self, index, value) -> bool:
        # check that is on the limits
        if index < 0 or index > self.length:
            return False
        #check if the node seaking is the first
        if index == 0:
            return self.prepend(value)
        # check if the node seaking is the last
        if index == self.length - 1:
            return self.append(value)
        # add new node
        new_value = Node(value)
        last_node_to_insert = self.get(index - 1)
        new_value.next = last_node_to_insert.next
        last_node_to_insert.next = new_value
        self.length += 1
        return True
    
    def remove(self, index) -> bool:
        # check that is on the limits
        if index < 0 or index >= self.length:
            return None
        #check if the node seaking is the first
        if index == 0:
            return self.pop_first()
        # check if the node seaking is the last
        if index == self.length - 1:
            return self.pop()
        # remove in the middle
        previous_last_node_to_remove = self.get(index - 1)
        last_node_to_remove = self.get(index)
        previous_last_node_to_remove.next = last_node_to_remove.next
        last_node_to_remove.next = None
        self.length -= 1
        return last_node_to_remove
        
    def reverse(self) -> None:
        # switch head and tail
        tmp_head = self.head
        self.head = self.tail
        self.tail = tmp_head
        # variables to switch the elements
        after = tmp_head.next
        before = None
        for _ in range(self.length):
            after = tmp_head.next
            tmp_head.next = before
            before = tmp_head
            tmp_head = after
        
    def print_list(self) -> None:
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end=" ")
            tmp = tmp.next