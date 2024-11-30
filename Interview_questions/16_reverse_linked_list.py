class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
reversed_list = reverse_linked_list(head)
