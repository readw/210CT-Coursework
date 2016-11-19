# Week 7 - 13) Write the pseudocode for an unweighted graph data structure. You
#              either use an adjacency matrix or an adjacency list approach.
#              Also, write a function to add a new node and a function to add
#              an edge. Following that, implement the graph you have designed in
#              the programming language of your choice. You may use your own
#              linked list from previous labs, the STL LL, or use a simple
#              fixed size array (10 elements would be fine).

'''
PSEUDOCODE
----------
CLASS UN_WEIGHTED
    INIT(self)
        self.adjList <- {}
        self.unweighted <- {}
        
    ADD_NODE(self, node)
        IF node NOT IN self.adjList:
            self.adjList[node] <- []
        ELSE
            RETURN NULL

    ADD_EDGE(self, node1, node2)
        IF (node1 IN self.adjList) AND (node2 IN self.adjList)
            IF node2 NOT IN self.adjList[node1]
                APPEND self.adjList[node1] WITH node2
            IF node1 NOT IN self.adjList[node2]
                APPEND self.adjList[node2] WITH node1
        ELSE
            RETURN NULL
'''

# Adjacency List Approach
class Unweighted:
    def __init__(self):
        '''Inital setup of instance - assigning adjList and the unweighted
variables to empty dictionaries.'''

        # Set empty dictionaries.
        self.adjList = {}
        self.unweighted = {}

    def addNode(self, node):
        '''Inserts a node into the adjacency list.'''
        # Check if node isn't in adjList
        if node not in self.adjList:
            # Assign the value of the new node to an empty list.
            self.adjList[node] = []
        # Otherwise, return error.
        else:
            print("ERROR: Node has already been inserted.")

    def addEdge(self, node1, node2):
        '''Adds an edge connection between two nodes that are in the adjList.'''
        # Determine if both node1 and node2 are in the adjList dictionary.
        if (node1 in self.adjList) and (node2 in self.adjList):
            # If node2 isn't in the values at key node1 in adjList, add to
            # values.
            if (node2 not in self.adjList[node1]):
                self.adjList[node1].append(node2)

            # If node1 isn't in the values at key node2 in adjList, add to
            # values.
            if (node1 not in self.adjList[node2]):
                self.adjList[node2].append(node1)
        # Otherwise, return error.
        else:
            print("ERROR: At least one of the nodes isn't present.")

    def generateGraph(self):
        '''Returns the full unweighted graph that has currently been created
based off of the '''
        # Loop through the key, value pairs, add key and value to final
        # unweighted graph dictionary.
        for key, value in self.adjList.items():
            # Determine if value isn't an empty array.
            if value != []:
                self.unweighted[key] = value

        # Return final unweighted graph to manipulate.
        return self.unweighted

if __name__ == "__main__":
    '''
    EXAMPLE GRAPH
    -------------
    The graph below is represented by the addNode and addEdge statements.

    A -- B -- C -- G -- I
    |  / |         |
    | /  |    J    |         K
    |    |    |    |
    D    E -- F    H
    '''
    graph = Unweighted()
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
    
    # Tests adding junk node
    graph.addNode("K")
    
    # Tests repeating Node
    graph.addNode("B")

    graph.addEdge("A","B")
    graph.addEdge("A","D")
    graph.addEdge("B","C")
    graph.addEdge("B","E")
    graph.addEdge("C","G")
    graph.addEdge("D","B")
    graph.addEdge("E","F")
    graph.addEdge("F","J")
    graph.addEdge("G","H")
    graph.addEdge("G","I")

    # Tests Duplication of edge
    graph.addEdge("B","C")

    # Tests Non-Existant values
    graph.addEdge("1","2")

    # Displays final Unweighted Adjacency List
    print(graph.generateGraph())
