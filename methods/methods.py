# Print a Linked List in reverse

# Input: [0, 1, 2, 3]

# Output:
# 3
# 2
# 1
# 0

def printLinkedListInReverse(lst):
    if (lst.next):
        printLinkedListInReverse(lst.next)
    
    print(lst.value)
    return