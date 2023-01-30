# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

#     def print_graph(self):
#         print('X|', end=" ")
#         for i in range(self.V):
#             print("{}|".format(i), end=" ")
#         print()
#         for i in range(self.V):
#             print("{}|".format(i), end=" ")
#             for j in range(self.V):
#                 print("{}|".format(self.graph[i][j]), end=" ")
#             print()

#     def add_edge(self, u, v):
#         self.graph[u][v] = 1
#         self.graph[v][u] = 1

# graph = Graph(7)
# graph.add_edge(0, 1)
# graph.add_edge(0, 3)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(1, 5)
# graph.add_edge(1, 6)
# graph.add_edge(2, 3)
# graph.add_edge(2, 5)gui
# graph.add_edge(2, 4)
# graph.add_edge(3, 4)
# graph.add_edge(4, 6)
# print("Adjacency Matrix:")
# graph.print_graph() 

class Graph:
    def __init__(self, vertices):
        self.V = len(vertices)
        self.vertices = vertices
        self.graph = [[0 for column in range(self.V)] for row in range(self.V)]
        self.vertex_map = {vertex: index for index, vertex in enumerate(vertices)}

    def print_graph(self):
        print('X|', end=" ")
        for vertex in self.vertices:
            print("{}|".format(vertex), end=" ")
        print()
        for i in range(self.V):
            print("{}|".format(self.vertices[i]), end=" ")
            for j in range(self.V):
                print("{}|".format(self.graph[i][j]), end=" ")
            print()

    def add_edge(self, u, v):
        u_index = self.vertex_map[u]
        v_index = self.vertex_map[v]
        self.graph[u_index][v_index] = 1

graph = Graph(["a", "b", "c", "d", "e", "f"])
graph.add_edge('a','b')
graph.add_edge('a','d')
graph.add_edge('b','c')
graph.add_edge('c','d')
graph.add_edge('d','e')
graph.add_edge('e','f')
graph.add_edge('e','b')
graph.add_edge('b','f')
graph.add_edge('f','a')
print("Adjacency Matrix for Directed Graphs:")
graph.print_graph()