
from node import Node

class SinglyLinkedList(object):

    def __init__(self):
        self.head = Node('head')
        self.tail = Node('tail')
        self.head.next = self.tail
        self.tail.next = self.tail
        self.length = 0
        return
        
    def get_length(self):
        return self.length
        
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1
        return
        
    def remove_from_front(self):
        # TODO
        return
        
    def insert_at_back(self, data):
        
        # Create Node
        new_node = Node(data, self.tail)
        
        current = self.head

        while current.next != self.tail:
            current = current.next
            
        current.next = new_node
        self.length += 1
        return
        
    def remove_from_back(self):
        # TODO
        return
        
    def print_list(self):
        current = self.head

        print("\nLinkedList:"),
        
        while current.next != self.tail:
            current = current.next
            print(current.data),
              
        print
        return

def test_insert_at_front():

    print("\n*** Testing insert_at_front() function ***")
 
    my_list = SinglyLinkedList()

    my_list.insert_at_front(5)
    my_list.insert_at_front(4)
    my_list.insert_at_front(3)
    my_list.insert_at_front(2)
    my_list.insert_at_front(1)

    my_list.print_list()

def test_insert_at_back():

    print("\n*** Testing insert_at_back() function ***")
 
    my_list = SinglyLinkedList()

    my_list.insert_at_back(1)
    my_list.insert_at_back(2)
    my_list.insert_at_back(3)
    my_list.insert_at_back(4)
    my_list.insert_at_back(5)

    my_list.print_list()

def test_length():

    print("\n*** Testing length() function ***")
 
    my_list = SinglyLinkedList()

    my_list.insert_at_front(5)
    my_list.insert_at_front(4)
    my_list.insert_at_front(3)
    my_list.insert_at_front(2)
    my_list.insert_at_front(1)

    print( "\nLength: " + str( my_list.get_length() ) )

def test_reverse():

    print("\n*** Testing reverse() function ***")
 
    # Create linked list
    my_list = SinglyLinkedList()

    # Add nodes to linked list
    my_list.insert_at_back(1)
    my_list.insert_at_back(2)
    my_list.insert_at_back(3)
    my_list.insert_at_back(4)
    my_list.insert_at_back(5)

    # Print linked list
    my_list.print_list()

    # Reverse linked list
    print("\nReversing list")
    my_list.reverse()

    # Print linked list
    my_list.print_list()

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ == '__main__':

    test_insert_at_front()
    test_insert_at_back()
    test_length()
    #test_reverse()

