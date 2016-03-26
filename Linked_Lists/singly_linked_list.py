
from node import Node

class SinglyLinkedList(object):

    def __init__(self):
        self.head = None
        return
        
    def reverse(self):
            
        result = None
        current = self.head
        next = None

        while current:
            next = current.next
            current.next = result
            result = current
            current = next

        self.head = result
            
        return
    
    def insert_at_front(self, data):
        
        # Create Node
        new_node = Node(data)
        
        # Set new_node.next = old head
        new_node.next = self.head
        
        # Set head = new_node
        self.head = new_node
        return
        
    def remove_from_front(self):
        # TODO
        return
        
    def insert_at_back(self, data):
        
        # Create Node
        new_node = Node(data)
        
        # If the list is empty, 
        if not self.head:
            self.head = new_node
        # Else, find the tail
        else:
            current = self.head

            while current.next:
                current = current.next
                
            current.next = new_node
        
        return
        
    def remove_from_back(self):
        # TODO
        return
        
    def print_list(self):
        current = self.head

        print("\nLinkedList:"),
        
        if current:
            print(current.data),

            while current.next:
                current = current.next
                print(current.data),
        else:
            print("(empty)")
              
        print
        return
        
    def length(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count

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

    print("\nLength: " + str(my_list.length()))

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

    #test_insert_at_front()
    #test_insert_at_back()
    #test_length()
    test_reverse()

