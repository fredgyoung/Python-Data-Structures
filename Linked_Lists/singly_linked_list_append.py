
from node import Node

class SinglyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        return
        
    def copy_node(self, node):
        new_node = Node(node.data, node.next)
        return new_node
        
    def insert_at_front(self, data):
        
        # Create Node
        new_node = Node(data)
        
        # If the list is empty then this new node will also become the tail
        if not self.head:
            self.tail = new_node
        
        # Set new_node.next = old head
        new_node.next = self.head
        
        # Set head = new_node
        self.head = new_node
        return

    # This function does not use self.tail
    def insert_at_back(self, data):
        
        # Create Node
        new_node = Node(data)
        
        # If the list is empty, 
        if not self.head:
            self.head = new_node
            self.tail = self.head
        # Else, find the tail
        else:
            current = self.head

            while current.next:
                current = current.next
                
            current.next = new_node
        
        return
        
    # This function uses self.tail
    def insert_at_tail(self, data):
        
        # Create Node
        new_node = Node(data)
        
        # If the list is empty, 
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
        
        return

    # WRONG: pass by reference, not value
    def append(self, other):
        current = other.head
        
        if current:
            self.insert_at_back(self.copy_node(current))
            
            while current.next:
                current = current.next
                
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

def test_append():

    list_a = SinglyLinkedList()
    list_b = SinglyLinkedList()

    list_a.insert_at_front(4)
    list_a.insert_at_front(3)
    list_a.insert_at_front(2)
    list_a.insert_at_front(1)
    list_a.insert_at_front(0)

    list_b.insert_at_front(9)
    list_b.insert_at_front(8)
    list_b.insert_at_front(7)
    list_b.insert_at_front(6)
    list_b.insert_at_front(5)

    list_a.print_list()
    list_b.print_list()
    
    list_a.append(list_b)
    del list_b

    list_a.print_list()

    #list_b.tail.data = 13
    #list_b.print_list()
    
    print
    print list_a.tail.data

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ == '__main__':

    test_append()

