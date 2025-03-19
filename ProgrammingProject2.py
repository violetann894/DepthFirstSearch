import math

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
        self.directed = directed
        self.time = 0

        for u in range(len(self.aList)):
            self.color.append("white")
            self.pi.append(None)
            self.d.append(0)
            self.f.append(0)

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
        self.time = 0
        self.DFSVisit(s)

        for u in range(len(self.aList)):
            if self.color[u] == "white":
                self.DFSVisit(u)

    """Visits the vertex and explores the connected vertices to see where the algorithm can move next"""
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
       s - The source vertex for DFS
       Returns: 
            linkedList - The linked list of vertices with the head node being the slowest finishing vertex
    """
    def TopologicalSort(self,s):

        """Run DFS"""
        self.DFS(s)

        """Create the stuff needed to create the decreasing finishing time list"""
        linkedList = None
        vertexAddedToList = []
        addedToList = 0
        smallestNumber = math.inf
        fastestVertex = None

        """Run through the list of finishing times and add the fastest vertex for each run so that eventually the head
        node of the linkedList is the slowest finishing vertex"""
        while addedToList < len(self.aList):
            for i in range(len(self.aList)):
                if smallestNumber > self.f[i] and self.f[i] not in vertexAddedToList:
                    smallestNumber = self.f[i]
                    fastestVertex = i
            if linkedList is None:
                linkedList = LinkedList(Node(fastestVertex))
            else:
                linkedList.listPrepend(fastestVertex)
            addedToList += 1
            vertexAddedToList.append(smallestNumber)
            smallestNumber = math.inf
            fastestVertex = None

        return linkedList

    """Using the vertices and edges of the graph, creates the transpose of that graph
       Returns: 
            graphT - The transposed graph object"""
    def Transpose(self):

        """Create the vertex list"""
        V = []
        for i in range(len(self.aList)):
            V.append(i)

        """Create the edges list"""
        E = []

        """Check to see if the graph is directed or not"""
        if self.directed:

            """If it is directed, then just add v,u to the edge list without any additional checks"""
            for u in range(len(self.aList)):
                for v in self.aList[u]:
                    E.append((v,u))
        else:
            """If it is not directed, then we need to check for duplicates ((u,v) and (v,u) are considered to be the 
            same edge in an undirected graph)"""
            for u in range(len(self.aList)):
                for v in self.aList[u]:
                    if (u,v) not in E and (v,u) not in E:
                        E.append((v,u))

        """Create the new transposed graph"""
        graphT = Graph(V, E, self.directed)

        return graphT

    """SCC stands for Strongly Connected Components. Strongly Connected Components are vertices that have a path from 
    u to v and a path from v to u. This algorithm checks to see if there are any Strongly connected components in the
    graph by running DFS, creating a list of decreasing finishing times, finding G^T and running DFS on G^T with the 
    list of decreasing finishing times in mind.
        s - The source to use for DFS"""
    def SCC(self, s):

        """Run DFS"""
        self.DFS(s)

        decreasingUF = []
        slowestVertex = -1

        """Create the decreasing finishing times list for the next part of the method"""
        while len(decreasingUF) < len(self.aList):
            largestNumber = -1
            for i in range(len(self.aList)):
                if largestNumber < self.f[i] and i not in decreasingUF:
                    largestNumber = self.f[i]
                    slowestVertex = i
            decreasingUF.append(slowestVertex)

        """Transpose the graph"""
        graphT = self.Transpose()

        """Complete the DFS visit on the transposed graph"""
        for u in decreasingUF:
            if graphT.color[u] == "white":
                graphT.DFS(u)

        StronglyConnected = []
        tree = []

        """Run through the predecessor list (pi) to see the trees that have formed from DFS"""
        for i in range(len(graphT.pi)):
            if graphT.pi[i] is None:
                if len(tree) != 0:
                    StronglyConnected.append(tree)
                tree = []
                tree.append(i)
            else:
                tree.append(i)
        StronglyConnected.append(tree)

        return StronglyConnected

if __name__ == "__main__":
    V = [0, 1, 2, 3, 4]
    E = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3)]

    graph = Graph(V, E, True)
    graph.printGraph()

    print()

    """Output a run using DFS"""
    graph.DFS(0)
    print(graph.color)
    print(graph.d)
    print(graph.f)
    print(graph.pi)
    print()

    """Output a run using topological sort"""
    graphTop = Graph(V, E, True)

    linkedList = graphTop.TopologicalSort(0)

    print()

    print(graph.color)
    print("Discovery times: ", graph.d)
    print("Finishing times: ", graph.f)

    linkedList.printLinkedList()

    print()

    """Output a run using Strongly Connected Components"""
    graphSCC = Graph(V, E, True)

    print("Strongly connected components trees: ", graphSCC.SCC(0))
