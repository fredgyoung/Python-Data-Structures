
class Node(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def set_data(self, data):
        self.data = data
        return

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left
        return
        
    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right
        return
        
    def get_right(self):
        return self.right

