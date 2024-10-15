class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Example 
linked_list = LinkedList()
linked_list.insert_at_beginning(1)
linked_list.insert_at_beginning(2)
linked_list.display()
