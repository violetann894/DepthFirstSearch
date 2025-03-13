import math


class Graph:
    """Creates an empty adjacency list called aList. This function uses a dictionary. You will be able to access the
        list per vertex by using v.
        V - A list of Vertices
        E - A list of Edges. This list needs to be a list of tuples.
        directed - Controls whehther the graph is a digraph or not"""

    def __init__(self, V, E, directed):
        self.aList = []

        for v in range(len(V)):
            self.aList.append([])

        for e in E:
            self.addEdge(e[0], e[1], directed)

    """Creates an edge. If directed is true, only one direction will be added. If not, both directions will be added
        v1 - The first vertex that makes up the edge
        v2 - The second vertex that makes up the edge
        directed - Controls whehther the graph is a digraph or not"""

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

    def DFS(self, s):

    ##Implement DFS from the psuedocode given in the slides (s is the source you want to start with. You will need this for SCC)

    def DFSVisit(self, u):

    ##Implement DFS Visit from the psuedocode given in the slides

    def TopologicalSort(self):

    ##Implement Topological Sort from the psuedocode given in the slides

    def Transpose(self):

    ##Implement a Graph Transopose to be used in the Strongly Connected Components function

    def SCC(self):


##Implement Strongly Connected Components from the psuedocode given in the slides

if __name__ == "__main__":
