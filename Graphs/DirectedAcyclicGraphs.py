'''
You are given a positive integer n representing the number of nodes of a
Directed Acyclic Graph (DAG) (Refer fig 4). The nodes are numbered from 0 to n - 1 (inclusive). You are also given a 2D integer array edges,
where edges[i] = [from i, to i] denotes that there is a unidirectional edge
from from i to to i in the graph. Return a list answer, where answer[i] is
the list of ancestors of the ith node, sorted in ascending order. A node u is
an ancestor of another node v if u can reach v via a set of edges.
Identify the traversal algorithm suitable to solve the problem. Modify the
algorithm and implement.
Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
'''

class DirectedAcyclicGraphs:
    def __init__(self, n, edgeList):
        self.n = n
        self.edgeList = edgeList
        self.adjList = [[] for _ in range(n)]
        self.ancestors = [[] for _ in range(n)]
        self.visited = [False for _ in range(n)]
        self.topoSort = []
        self.buildAdjList()
        self.topologicalSort()
        self.findAncestors()

    def buildAdjList(self):
        for edge in self.edgeList:
            self.adjList[edge[0]].append(edge[1])

    def topologicalSort(self):
        for node in range(self.n):
            if not self.visited[node]:
                self.dfs(node)
        self.topoSort.reverse()

    def dfs(self, node):
        self.visited[node] = True
        for neighbour in self.adjList[node]:
            if not self.visited[neighbour]:
                self.dfs(neighbour)
        self.topoSort.append(node)

    def findAncestors(self):
        for node in self.topoSort:
            for neighbour in self.adjList[node]:
                self.ancestors[neighbour].append(node)
                self.ancestors[neighbour].extend(self.ancestors[node])
            self.ancestors[node] = list(set(self.ancestors[node]))

    def getAncestors(self):
        return self.ancestors

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
dag = DirectedAcyclicGraphs(n, edgeList)
print(dag.getAncestors())