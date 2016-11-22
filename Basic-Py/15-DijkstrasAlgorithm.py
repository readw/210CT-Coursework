# Week 8 - 15) Implement Dijkstras algorithm for a weighted graph data structure
#              (you have to update your previous data structure so that it can
#              deal with weights).
class Weighted:

    def __init__(self):
        self.weighted = {}

    def addNode(self, node):
        if node not in self.weighted:
            self.weighted[node] = {}
        else:
            print("ERROR: Node has already been inserted.")

    def addEdge(self, node1, node2, length):
        if (node1 in self.weighted) and (node2 in self.weighted):
            if (node2 not in self.weighted[node1]):
                self.weighted[node1][node2] = length
            if (node1 not in self.weighted[node2]):
                self.weighted[node2][node1] = length
        else:
            print("ERROR: At least one of the nodes isn't present.")
    
    def displayGraph(self):
        return self.weighted
    

def Dijkstras(graph, start, end):
    pass

if __name__ == "__main__":
    '''
    EXAMPLE GRAPH
    -------------
    The graph below is represented by the addNode and addEdge statements.

    A -(2)- B -(1)- C -(1)- G -(2)- I
    |     / |               |
  (1)  (3) (1)      J      (4)
    | /     |      (1)      |
    D       E -(2)- F       H
    '''
    
    graph = Weighted()
    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addNode("D")
    graph.addNode("E")
    graph.addNode("F")
    graph.addNode("G")
    graph.addNode("H")
    graph.addNode("I")
    graph.addNode("J")

    graph.addEdge("A","B",2)
    graph.addEdge("A","D",1)
    graph.addEdge("B","C",1)
    graph.addEdge("B","E",1)
    graph.addEdge("C","G",1)
    graph.addEdge("D","B",3)
    graph.addEdge("E","F",2)
    graph.addEdge("F","J",1)
    graph.addEdge("G","H",4)
    graph.addEdge("G","I",2)

    weightedGraph = graph.displayGraph()

    print(weightedGraph)
    print(Dijkstras(graph, 'A', 'J'))
