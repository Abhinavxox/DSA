class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    def __init__(self):
        self.vertices = {}
        self.visited = []
        self.queue = []

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    def bfs(self, vertex):
        self.visited = []
        self.queue = []
        self.queue.append(vertex)
        self.visited.append(vertex)
        while self.queue:
            m = self.queue.pop(0)
            print(m, end=" ")

            for neighbor in self.vertices[m].neighbors:
                if neighbor not in self.visited:
                    self.visited.append(neighbor)
                    self.queue.append(neighbor)

    def dfs(self, vertex):
        self.visited = []
        self.dfs_helper(vertex)
        
    def dfs_helper(self, vertex):
        self.visited.append(vertex)
        print(vertex, end=" ")

        for neighbor in self.vertices[vertex].neighbors:
            if neighbor not in self.visited:
                self.dfs_helper(neighbor)
    


graph = Graph()
graph.add_vertex(Vertex('A'))
graph.add_vertex(Vertex('B'))
graph.add_vertex(Vertex('C'))
graph.add_vertex(Vertex('D'))
graph.add_vertex(Vertex('E'))
graph.add_vertex(Vertex('F'))
graph.add_vertex(Vertex('G'))
graph.add_vertex(Vertex('H'))
graph.add_vertex(Vertex('I'))
graph.add_vertex(Vertex('J'))

edges = ['AB', 'BC', 'ED', 'FD', 'DG', 'DH', 'HI', 'IJ', 'JG','FG']
for edge in edges:
    graph.add_edge(edge[:1], edge[1:])

# print("BFS Traversal: ")
# graph.bfs('A')
# print()

print("DFS Traversal: ")
graph.dfs('G')
print()