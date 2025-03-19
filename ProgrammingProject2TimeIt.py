import timeit

setUp="""
import math

class Node:

    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self, head):
        self.head = head

    def listSearch(L, k):
        x = L.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def listPrepend(L, k):
        x = Node(k)
        x.next = L.head
        x.prev = None
        if L.head is not None:
            L.head.prev = x
        L.head = x

    def listInsert(L, x, y):
        x.next = y.next
        x.prev = y
        if y.next is not None:
            y.next.prev = x
        y.next = x

    def listDelete(L, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            L.head = x.next
            if x.next is not None:
                x.next.prev = x.prev

    def printLinkedList(L):
        x = L.head
        while x is not None:
            print(x.key)
            x = x.next

class Graph:

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

    def addEdge(self, v1, v2, directed):
        if not directed:
            self.aList[v1].append(v2)
            self.aList[v2].append(v1)
        else:
            self.aList[v1].append(v2)

    def printGraph(self):
        count = 0
        for v in self.aList:
            print(count, ": ", v)
            count = count + 1

    def degree(self, v):
        return len(self.aList[v])

    def DFS(self, s):
        self.time = 0
        self.DFSVisit(s)
        for u in range(len(self.aList)):
            if self.color[u] == "white":
                self.DFSVisit(u)

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

    def TopologicalSort(self,s):
        self.DFS(s)
        linkedList = None
        vertexAddedToList = []
        addedToList = 0
        smallestNumber = math.inf
        fastestVertex = None
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

    def Transpose(self):
        V = []
        for i in range(len(self.aList)):
            V.append(i)
        E = []
        if self.directed:
            for u in range(len(self.aList)):
                for v in self.aList[u]:
                    E.append((v,u))
        else:
            for u in range(len(self.aList)):
                for v in self.aList[u]:
                    if (u,v) not in E and (v,u) not in E:
                        E.append((v,u))
        graphT = Graph(V, E, self.directed)
        return graphT

    def SCC(self, s):
        self.DFS(s)
        decreasingUF = []
        slowestVertex = -1
        while len(decreasingUF) < len(self.aList):
            largestNumber = -1
            for i in range(len(self.aList)):
                if largestNumber < self.f[i] and i not in decreasingUF:
                    largestNumber = self.f[i]
                    slowestVertex = i
            decreasingUF.append(slowestVertex)
        graphT = self.Transpose()
        for u in decreasingUF:
            if graphT.color[u] == "white":
                graphT.DFS(u)
        StronglyConnected = []
        tree = []
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
"""

if __name__ == "__main__":
    DFS="""
V = [0, 1, 2, 3, 4]
E = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3)]
graph = Graph(V, E, True)
graph.DFS(0)"""

    DFSLessVertices= """
V = [0,1,2,3]
E = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
graph = Graph(V, E, True)
graph.DFS(0)"""

    topological="""
V = [0, 1, 2, 3, 4]
E = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3)]
graph = Graph(V, E, True)
graph.TopologicalSort(0)"""

    topologicalLessVertices= """
V = [0,1,2,3]
E = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
graph = Graph(V, E, True)
graph.TopologicalSort(0)"""

    SCC="""
V = [0, 1, 2, 3, 4]
E = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3)]
graph = Graph(V, E, True)
graph.SCC(0)"""

    SCCLessVertices= """
V = [0,1,2,3]
E = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
graph = Graph(V, E, True)
graph.SCC(0)"""

print("DFS: ", timeit.timeit(setup = setUp, stmt = DFS, number=1000000))
print("DFS with less vertices: ", timeit.timeit(setup = setUp, stmt = DFSLessVertices, number=1000000))
print("Topological Sort: ", timeit.timeit(setup = setUp, stmt = topological, number=1000000))
print("Topological Sort with less vertices: ", timeit.timeit(setup = setUp, stmt = topologicalLessVertices,
                                                             number=1000000))
print("Strongly Connected Components: ", timeit.timeit(setup = setUp, stmt = SCC, number=1000000))
print("Strongly Connected Components with less vertices: ", timeit.timeit(setup = setUp, stmt = SCCLessVertices,
                                                                          number=1000000))