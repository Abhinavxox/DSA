class Graph:
    vertices = {}

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

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + " : " + str(self.vertices[key].neighbors))

# graph = Graph()
# graph.add_vertex(Vertex('0'))
# graph.add_vertex(Vertex('1'))
# graph.add_vertex(Vertex('2'))
# graph.add_vertex(Vertex('3'))
# graph.add_vertex(Vertex('4'))
# graph.add_vertex(Vertex('5'))
# graph.add_vertex(Vertex('6'))

# edges = ['01', '03', '12', '13', '15', '16', '23', '25', '24','34','46']
# for edge in edges:
#     graph.add_edge(edge[:1], edge[1:])
# graph.print_graph()

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class DirectedGraph:
    vertices = {}

    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
    
    def add_directed_edge(self,u,v):
        if u in self.vertices:
            self.vertices[u].add_neighbor(v)

    def print_directed_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+" : "+ str(self.vertices[key].neighbors))

graph = DirectedGraph()
graph.add_vertex(Vertex('a'))
graph.add_vertex(Vertex('b'))
graph.add_vertex(Vertex('c'))
graph.add_vertex(Vertex('d'))
graph.add_vertex(Vertex('e'))
graph.add_vertex(Vertex('f'))

graph.add_directed_edge('a','b')
graph.add_directed_edge('b','c')
graph.add_directed_edge('c','d')
graph.add_directed_edge('d','e')
graph.add_directed_edge('e','f')
graph.add_directed_edge('f','a')
graph.add_directed_edge('a','d')
graph.add_directed_edge('e','b')
graph.add_directed_edge('b','f')

graph.print_directed_graph()
