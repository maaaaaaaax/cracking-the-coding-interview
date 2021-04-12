# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

linked_list = Node(2)

# Add a node
temp = linked_list
while temp.next:
    temp = temp.next
temp.next = Node(3)

# Add a node
temp = linked_list
while temp.next:
    temp = temp.next
temp.next = Node(3)

# Add a node
temp = linked_list
while temp.next:
    temp = temp.next
temp.next = Node(3)

# Add a node 
temp = linked_list
while temp.next:
    temp = temp.next
temp.next = Node(4)

# Print the list
temp = linked_list
while temp:
    print(temp.data)
    temp = temp.next

print()

# Remove duplicates
seen = set()
current_node = linked_list
previous_node = linked_list
while current_node:
    # If the current data has not been seen, add it to the set, set previous to current, then increment current_node
    if current_node.data not in seen:
        seen.add(current_node.data)
        previous_node = current_node
        current_node = current_node.next

    # If the current data has been seen, set previous.next to current_node.next, then increment current_node
    else:
        previous_node.next = current_node.next
        current_node = current_node.next

# Print the list
temp = linked_list
while temp:
    print(temp.data)
    temp = temp.next