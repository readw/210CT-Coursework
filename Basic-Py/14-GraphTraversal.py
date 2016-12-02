# Week 7 - 14) Implement BFS and DFS traversals for the above graph. Save the
#              nodes traversed in sequence to a text file.

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

class Traversal:
    def __init__(self, graph):
        self.graph = graph

    # Breadth First Search Function
    def BFS(self, start):
        '''Function to perform a breadth first traversal from a given root.'''
        # Assign traversal order and queue with start value in array.
        traversalOrder, queue = [start], [start]

        # While the queue contains a value.
        while queue and (len(traversalOrder) != len(self.graph)):
            # Pop the first value on the queue and store at current.
            current = queue.pop()
            if current not in traversalOrder:
                traversalOrder.append(current)
                
            # For all the assigned neighbours to the key 'current'
            for neighbour in self.graph[current]:
                # Check to see if the item hasn't been added to the traversal
                # yet, then append the value to both the traversal order,
                # and the queue.
                queue.insert(0,neighbour)
        # Returns the result of the breadth first.
        return traversalOrder

    # Iterative Depth First Search Function
    def DFS(self, start):
        '''Function to perform a depth first traversal from a given root.'''
        # Assign an empty array to traversalOrder and assign an array to stack
        # with the root node (starting value).
        traversalOrder, stack = [], [start]

        # Whilst there is a value in the stack
        while stack:
            # Set current to item at the top of the stack.
            current = stack.pop()
            # If the current node isn't in the traversalOrder array.
            if current not in traversalOrder:
                # Append this to the traversalOrder.
                traversalOrder.append(current)
                # And for all assigned nodes to the key 'current'
                for node in self.graph[current]:
                    # Append the node to the end of the stack.
                    stack.append(node)

        # Returns the result of the Depth First Search.
        return traversalOrder

if __name__ == "__main__":
    '''
    EXAMPLE GRAPH
    -------------
    The graph below is represented by the addNode and addEdge statements.

    A -- B -- C -- G -- I
    |  / |         |
    | /  |    J    |
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

    # Displays final Unweighted Adjacency List
    resultGraph = graph.generateGraph()

    #Traversal Calls
    traversal = Traversal(resultGraph)
    file = open('results.txt', 'w')
    print(traversal.BFS('C'))
    print(traversal.DFS('C'))
    file.write(str(traversal.BFS('C'))+'\n')
    file.write(str(traversal.DFS('C'))+'\n')
    file.close()
