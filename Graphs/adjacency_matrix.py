
class AdjacencyMatrix(object):

    def __init__(self, vertices=0):
        self.size = vertices
        self.matrix = [[0 for col in range(self.size)] for row in range(self.size)]
        
    def set_edge(self, start, end, directed=False, weight=1):
        self.matrix[start][end] = weight
        
        if directed == False:
            self.matrix[end][start] = weight
            
    def print_matrix(self):
        
        print "\nGraph\n"
        
        print '  ',
        for col in range(1, self.size+1):
            print '%d ' % col,
         
        print
        count = 0
        
        for row in self.matrix:
            count += 1
            print count, 
            print row
        
def undirected():
    graph = AdjacencyMatrix(5)

    graph.print_matrix()

    graph.set_edge(0, 1)
    graph.set_edge(0, 4)
    graph.set_edge(1, 2)
    graph.set_edge(1, 3)
    graph.set_edge(1, 4)
    graph.set_edge(2, 3)
    graph.set_edge(3, 4)

    graph.print_matrix()

def directed():
    graph = AdjacencyMatrix(5)

    graph.print_matrix()

    graph.set_edge(0, 1, directed=True)
    graph.set_edge(0, 4, directed=True)
    graph.set_edge(1, 2, directed=True)
    graph.set_edge(1, 3, directed=True)
    graph.set_edge(1, 4, directed=True)
    graph.set_edge(2, 3, directed=True)
    graph.set_edge(3, 4, directed=True)

    graph.print_matrix()
    
if __name__ == '__main__':

    undirected()
    #directed()
    