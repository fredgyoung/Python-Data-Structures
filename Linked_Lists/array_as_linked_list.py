
class ArrayAsLinkedList(object):

    def __init__(self):
        self.array = []
        self.array.append(['head', 1])
        self.array.append(['tail', 0])
        return
        
    def insert_at_front(self, data):
        self.array.append([data, len(self.array) - 1])
        self.array[0][1] = len(self.array) - 1
        return
        
    def print_list(self):
        print("\nLinkedList:"),

        index = 0
        current = self.array[index]
        print self.array[index][0],

        while self.array[index][1] != 0:
            index = self.array[index][1]
            print self.array[index][0],
                    
        print
        return
        
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ == '__main__':

    my_array = ArrayAsLinkedList()
    my_array.insert_at_front('c')
    my_array.insert_at_front('b')
    my_array.insert_at_front('a')
    my_array.print_list()
    

