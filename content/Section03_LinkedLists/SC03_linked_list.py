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
    
    def remove(self, index, value) -> bool:
        pass
    
    def print_list(self) -> None:
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end=" ")
            tmp = tmp.next
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
#my_linked_list.append(3)
#my_linked_list.append(4)
#print(my_linked_list.length)
my_linked_list.print_list()
print(f"\nHead: {my_linked_list.head.value} Tail: {my_linked_list.tail.value}")

my_linked_list.prepend(11)
my_linked_list.prepend(10)
my_linked_list.prepend(8)
my_linked_list.print_list()
print(f"\nHead: {my_linked_list.head.value} Tail: {my_linked_list.tail.value}")

# my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.pop_first()

print(my_linked_list.get(2))
print(my_linked_list.get(-2))
print(my_linked_list.get(4))
print(my_linked_list.get(3))
print(my_linked_list.set_value(0,19))
print(my_linked_list.set_value(4,85))


#print(my_linked_list.get2(2))
#print(my_linked_list.get2(0))

my_linked_list.print_list()
print(f"\nHead: {my_linked_list.head.value} Tail: {my_linked_list.tail.value}")

print(my_linked_list.insert(3,55))
print(my_linked_list.insert(2,54))
print(my_linked_list.insert(7,44))
my_linked_list.print_list()
print(f"\nHead: {my_linked_list.head.value} Tail: {my_linked_list.tail.value}")

# print(my_linked_list.pop()) # 2 
# print(my_linked_list.pop()) # 1
# print(my_linked_list.pop()) # 0
#print(f"\nHead: {my_linked_list.head.value} Tail: {my_linked_list.tail.value}")