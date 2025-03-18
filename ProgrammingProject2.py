class Node:
    """The constructor for the Node class creates a new Node object that holds information about the current state
        of the Node.
        key - The data that the Node needs to hold
        next - The pointer to the next object, starts as none because nothing is connected to a newly created Node
        prev - The pointer to the previous object, starts as none because nothing is connected to a newly created node
        """

    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    """The constructor for the LinkedList class creates a new LinkedList object.
        head - The Node at the beginning of the list"""

    def __init__(self, head):
        self.head = head

    """listSearch accepts a key value for a Node in the LinkedList and returns if the Node was found.
        k - The key value for the desired Node

        Return x - The Node with the key value given, returns none if the Node was not found"""

    def listSearch(L, k):
        x = L.head
        while x is not None and x.key != k:
            x = x.next
        return x

    """listPrepend accepts a key value for a Node, creates a new Node object and adds it to the beginning of the 
        linked list.
        k - The key value for the new head Node"""

    def listPrepend(L, k):
        x = Node(k)
        x.next = L.head
        x.prev = None
        if L.head is not None:
            L.head.prev = x
        L.head = x

    """listInsert inserts a Node after a chosen Node.
        x - The Node to be inserted after y
        y - The Node that x will be inserted after"""

    def listInsert(L, x, y):
        x.next = y.next
        x.prev = y
        if y.next is not None:
            y.next.prev = x
        y.next = x

    """listDelete deletes the desired node in the linked list.
        x - The Node object to be deleted from the list"""

    def listDelete(L, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            L.head = x.next
            if x.next is not None:
                x.next.prev = x.prev

    """printLinkedList prints out the key values of the linked list, with the value at the top being the 
        key value of the head of the list."""

    def printLinkedList(L):
        x = L.head
        while x is not None:
            print(x.key)
            x = x.next

class Graph:
    """Creates an empty adjacency list called aList. This function uses a dictionary. You will be able to access the
        list per vertex by using v.
        V - A list of Vertices
        E - A list of Edges. This list needs to be a list of tuples.
        directed - Controls whether the graph is a digraph or not"""

    def __init__(self, V, E, directed):
        self.aList = []

        for v in range(len(V)):
            self.aList.append([])

        for e in E:
            self.addEdge(e[0], e[1], directed)

        self.color = []
        self.pi = []
        self.d = []
        self.f = []

    """Creates an edge. If directed is true, only one direction will be added. If not, both directions will be added
        v1 - The first vertex that makes up the edge
        v2 - The second vertex that makes up the edge
        directed - Controls whether the graph is a digraph or not"""

    def addEdge(self, v1, v2, directed):
        if not directed:
            self.aList[v1].append(v2)
            self.aList[v2].append(v1)
        else:
            self.aList[v1].append(v2)

    """Prints the Adjacency List."""

    def printGraph(self):
        count = 0
        for v in self.aList:
            print(count, ": ", v)
            count = count + 1

    """Returns the degree of specified vertex.
        v - The vertex you want to get the degree of
        Return:
            len(self.aList[v]) - The number of edges coming out of the vertex."""

    def degree(self, v):
        return len(self.aList[v])

    """Runs Depth First Search on the Graph object using s as the source
        s - Source vertex for DFS"""

    def DFS(self, s):

        """This sets up the lists for the DFS search"""
        for u in range(len(self.aList)):
            self.color.append("white")
            self.pi.append(None)
            self.d.append(0)
            self.f.append(0)

        """This actually begins the DFS algorithm"""
        self.time = 0
        for u in range(len(self.aList)):
            if self.color[u] == "white":
                self.DFSVisit(u)

    """Vists the vertex and explores the connected vertices to see where the algorithm can move next"""

    def DFSVisit(self, u):
        self.time += 1
        self.d[u] = self.time
        self.color[u] = "grey"
        for v in self.aList[u]:
            if self.color[v] == "white":
                self.pi[v] = u
                self.DFSVisit(v)
        self.color[u] = "black"
        self.time += 1
        self.f[u] = self.time

    """Runs DFS on the list and then creates a linked list of objects sorted in topological order
    Returns: """
    def TopologicalSort(self):



    """"""
    #def Transpose(self):
    ##Implement a Graph Transpose to be used in the Strongly Connected Components function



    """"""
    #def SCC(self):
    ##Implement Strongly Connected Components from the psuedocode given in the slides



if __name__ == "__main__":
    V = [0, 1, 2, 3]
    E = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]

    graph = Graph(V, E, False)
    graph.printGraph()

    print()

    graph.DFS(1)
    print(graph.color)
    print(graph.d)
    print(graph.f)
    print(graph.pi)