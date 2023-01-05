#implement adjacency matrix in py

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_graph(self):
        print('X|', end=" ")
        for i in range(self.V):
            print("{}|".format(i), end=" ")
        print()
        for i in range(self.V):
            print("{}|".format(i), end=" ")
            for j in range(self.V):
                print("{}|".format(self.graph[i][j]), end=" ")
            print()

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 5)
graph.add_edge(1, 6)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 6)
print("Adjacency Matrix:")
graph.print_graph()

