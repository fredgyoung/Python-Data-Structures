
from node import Node
import copy
import sys

class SinglyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        return
        
    def copy_node(self, node):
        new_node = Node(node.data, node.next)
        return new_node
        
    # def copy(self):
        # print("Inside copy()")
        # new_list = SinglyLinkedList()
        
        # if self.head == None:
            # return new_list
            
        # # Iterate over old list. Make a copy of each node and insert into new list.
        # current = self.head
        # new_list.insert_at_back(self.copy_node(current))
        
        # while current.next:
            # current = current.next
            # new_list.insert_at_back(self.copy_node(current))
        
        # return new_list
        
    def copy(self):
        return copy.deepcopy(self)
        
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
    def insert_at_back(self, data, next=None):
        print("Inside insert_at_back()")
        
        # Create Node
        new_node = Node(data, next)
        
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

def test_copy():

    list_a = SinglyLinkedList()

    list_a.insert_at_front(4)
    list_a.insert_at_front(3)
    list_a.insert_at_front(2)
    list_a.insert_at_front(1)
    list_a.insert_at_front(0)

    list_b = list_a.copy()

    list_a.print_list()
    list_b.print_list()
    
    print list_a
    print list_b
    
    print sys.getsizeof(list_a)
    
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ == '__main__':

    test_copy()

