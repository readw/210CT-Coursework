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
    '''Performs Dijkstras Algorithm to traverse the graph from start to
end over a weighted graph.'''
    # Assign current
    current = start
    visited = []
    # Set previously visited nodes 
    previous, tentativeWeights = {}, {}

    # Assign all tentative weights for all nodes to infinity.
    for node in graph:
        tentativeWeights[node] = float("inf")
        previous[node] = None
        
    # Default start weight as 0.
    tentativeWeights[start] = 0
    
    # Until the current value matches the end result.
    while current != end:
        # Define neighbours
        neighbours = graph[current]
        for edge in neighbours:
            # If distance less than what is currently set.
            if tentativeWeights[current]+neighbours[edge] < tentativeWeights[edge]:
                # Assign edge to the smaller distance.
                tentativeWeights[edge] = tentativeWeights[current]+neighbours[edge]
                previous[edge] = current
        # Append current value to the visited path array.
        visited.append(current)
        # Set minimum value to infinity.
        minimum = float("inf")
        for node in graph:
            # Check to see if the value isn't in visited and that the weight
            # is less than that of the minimum path.
            if (node not in visited) and (tentativeWeights[node] < minimum):
                # Assign the current value to the new node.
                current = node
                # Set the minimum value to the new weight.
                minimum = tentativeWeights[node]

    visited.append(end)
    
    # Generate a path from collected data.
    path = shortestPath(previous, end)
    # Return formatted output
    return "Distance: "+str(tentativeWeights[end])+"\nPath: "+str(path)
    
def shortestPath(previous, end):
    # Create array to store the result.
    result = []
    # Until it reaches parent node.
    while previous[end] != None:
        # Add end connection to array.
        result.append(end)
        # Set end to it's closest neighbour.
        end = previous[end]
    # Append the parent to the reuslt and return the shortest path.
    result.append(end)
    return result[::-1]

if __name__ == "__main__":
    '''
    EXAMPLE GRAPH
    -------------
    The graph below is represented by the addNode and addEdge statements.

    A -(2)- B -(1)- C -(1)- G -(2)- I
    |     / |               |
  (1)  (3) (1)      J      (3)
    | /     |      (1)      |
    D       E -(2)- F -(2)- H
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
    graph.addEdge("F","H",2)
    graph.addEdge("G","H",3)
    graph.addEdge("G","I",2)

    weightedGraph = graph.displayGraph()

    # Uncomment to view weighted graph that has been generated.
    #print(weightedGraph)

    # Calculate the shortest path using Dijkstras Algorithm.
    print(Dijkstras(weightedGraph, 'A', 'J'))
