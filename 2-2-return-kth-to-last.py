# 2.2 Return Kth to Last

# Implement an algorithm to find the kth to last element of a singly linked list. Page 94, Cracking the Coding Interview, 6th Edition.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Prints a linked list
def print_linked_list(linked_list):
    temp = linked_list
    while temp:
        print(temp.data)
        temp = temp.next

# Adds a node to the end of a given linked list
def insert_node(linked_list, node):
    temp = linked_list
    while temp.next:
        temp = temp.next
    temp.next = node

# Create a linked list with one node
linked_list = Node(2)

# Print the linked list as a sanity check
print_linked_list(linked_list)

# Insert four nodes at the end
insert_node(linked_list, Node(4))
insert_node(linked_list, Node(6))
insert_node(linked_list, Node(8))
insert_node(linked_list, Node(10))

# Print the linked list as a sanity check
print_linked_list(linked_list)

def return_kth_to_last(k, linked_list):
    temp = linked_list
    runner = linked_list
    count = 0
    while count < k:
        if not runner.next:
            return False
        runner = runner.next
        count += 1
    while runner:
        runner = runner.next
        temp = temp.next
    return temp.data

print(return_kth_to_last(3, linked_list))