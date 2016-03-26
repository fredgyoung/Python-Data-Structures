
from node import Node
import unittest

class TestNode(unittest.TestCase):

    def setUp(self):
        self.node1 = Node()
        self.node2 = Node()
        
    def tearDown(self):
        self.node1 = None
        self.node2 = None
    
    def test_get_set_data(self):
        self.node1.set_data(5)
        self.assertEqual(self.node1.get_data(), 5)    
    
    def test_get_set_next(self):
        self.node1.set_next(self.node2)
        self.assertEqual(self.node1.get_next(), self.node2)    
        
if __name__ == '__main__':
    unittest.main()
    