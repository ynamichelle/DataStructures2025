class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        """Delete the first node with the given key (data)."""
        current_node = self.head

        # If the head node itself holds the key
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Search for the key to be deleted
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        # If the key was not present in the list
        if not current_node:
            return

        # Unlink the node from the linked list
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        """Display the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.display()  # Output: 1 -> 2 -> 3 -> None

    ll.delete_node(2)
    ll.display()  # Output: 1 -> 3 -> None

    ll.delete_node(1)
    ll.display()  # Output: 3 -> None

    ll.delete_node(3)
    ll.display()  # Output: None