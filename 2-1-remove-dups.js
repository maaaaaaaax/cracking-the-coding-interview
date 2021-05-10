// 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

let linked_list = new Node(2);

// Prints a linked list
function print_list(linked_list)
{
    let temp = linked_list;
    while (temp)
    {
        console.log(temp.data);
        temp = temp.next;
    }
}

// Print the list as a sanity check
// print_list(linked_list);

// Adds a node to the end of the list
function add_node(linked_list, node)
{
    let current_node = linked_list;
    while (current_node.next)
    {
        current_node = current_node.next;
    }
    current_node.next = node;
}

// Add three nodes to the end of the list
add_node(linked_list, new Node(4));
add_node(linked_list, new Node(6));
add_node(linked_list, new Node(6));
add_node(linked_list, new Node(6));
add_node(linked_list, new Node(8));
add_node(linked_list, new Node(8));

// Print the list as a sanity check
// print_list(linked_list);
// console.log();

// Remove duplicates from an unsorted linked list
function remove_duplicates(linked_list)
{
    let temp = linked_list;
    let seen = new Set();
    while (temp.next)
    {
        seen.add(temp.data);
        if (seen.has(temp.next.data))
        {
            temp.next = temp.next.next;
        }
        else
        {
            temp = temp.next;
        }
    }
}

remove_duplicates(linked_list);
print_list(linked_list);