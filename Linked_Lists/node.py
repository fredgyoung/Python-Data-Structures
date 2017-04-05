
class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data
        return

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next
        return
        
    def get_next(self):
        return self.next

