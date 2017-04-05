
# Doubly Linked List

class Node(object):

    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev
        
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next
        
class DoublyLinkedList(object):

    def __init__(self):
        
        # Create sentinels
        self.head = Node(None)
        self.tail = Node(None)
        
        # Connect sentinels
        self.head.next = tail
        self.tail.prev = head
        
    def insert(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node
        
    def print_list(self):
        current = self.head

        if current:
            print(current.data),

        while current.next:
            current = current.next
            print(current.data),
            
    def length(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count

my_list = LinkedList()

my_list.insert(5)
my_list.insert(7)
my_list.insert(2)

print("\nLength: " + str(my_list.length()) + "\n")

my_list.print_list()

