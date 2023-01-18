# class Vertex:
#     def __init__(self, n):
#         self.name = n
#         self.neighbors = list()
#         self.color = 'black'

#     def add_neighbor(self, v):
#         if v not in self.neighbors:
#             self.neighbors.append(v)
#             self.neighbors.sort()

# class Graph:
#     def __init__(self):
#         self.vertices = {}
#         self.visited = []
#         self.queue = []

#     def add_vertex(self, vertex):
#         if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
#             self.vertices[vertex.name] = vertex

#     def add_edge(self, u, v):
#         if u in self.vertices and v in self.vertices:
#             for key, value in self.vertices.items():
#                 if key == u:
#                     value.add_neighbor(v)
#                 if key == v:
#                     value.add_neighbor(u)

#     def bfs(self, vertex):
#         self.visited = []
#         self.queue = []
#         self.queue.append(vertex)
#         self.visited.append(vertex)
#         while self.queue:
#             m = self.queue.pop(0)
#             print(m, end=" ")

#             for neighbor in self.vertices[m].neighbors:
#                 if neighbor not in self.visited:
#                     self.visited.append(neighbor)
#                     self.queue.append(neighbor)

#     def dfs(self, vertex):
#         self.visited = []
#         self.dfs_helper(vertex)
        
#     def dfs_helper(self, vertex):
#         self.visited.append(vertex)
#         print(vertex, end=" ")

#         for neighbor in self.vertices[vertex].neighbors:
#             if neighbor not in self.visited:
#                 self.dfs_helper(neighbor)
    


# graph = Graph()
# graph.add_vertex(Vertex('A'))
# graph.add_vertex(Vertex('B'))
# graph.add_vertex(Vertex('C'))
# graph.add_vertex(Vertex('D'))
# graph.add_vertex(Vertex('E'))
# graph.add_vertex(Vertex('F'))
# graph.add_vertex(Vertex('G'))
# graph.add_vertex(Vertex('H'))
# graph.add_vertex(Vertex('I'))
# graph.add_vertex(Vertex('J'))

# edges = ['AB', 'BC', 'ED', 'FD', 'DG', 'DH', 'HI', 'IJ', 'JG','FG']
# for edge in edges:
#     graph.add_edge(edge[:1], edge[1:])

# # print("BFS Traversal: ")
# # graph.bfs('A')
# # print()

# print("DFS Traversal: ")
# graph.dfs('G')
# print()

class Graph:
    def __init__(self, vertices):
        self.V = len(vertices)
        self.vertices = vertices
        self.graph = [[0 for column in range(self.V)] for row in range(self.V)]
        self.vertex_map = {vertex: index for index, vertex in enumerate(vertices)}

    def add_edge(self, u, v):
        u_index = self.vertex_map[u]
        v_index = self.vertex_map[v]
        self.graph[u_index][v_index] = 1

    def bfs(self, vertex):
        self.visited = []
        self.queue = []
        self.queue.append(vertex)
        self.visited.append(vertex)
        while self.queue:
            m = self.queue.pop(0)
            print(m, end=" ")

            for neighbor in range(self.V):
                if self.graph[self.vertex_map[m]][neighbor] and self.vertices[neighbor] not in self.visited:
                    self.visited.append(self.vertices[neighbor])
                    self.queue.append(self.vertices[neighbor])


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

graph.bfs('a')
print()
