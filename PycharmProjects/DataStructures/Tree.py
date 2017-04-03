
class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        return

    def set_data(self, data):
        self.data = data
        return

    def get_data(self):
        return self.data

    def set_left_child(self, left_child):
        self.left_child = left_child
        return

    def get_left_child(self):
        return self.left_child

    def set_right_child(self, right_child):
        self.right_child = right_child
        return

    def get_right_child(self):
        return self.right_child

    def has_next(self):
        return self.next is not None


