class Graph:
    def __init__(self, gdict=None):
        if not gdict:
            self.gdict = {}
        self.gdict = gdict

    def print_dict(self):
        return self.gdict

    def print_vertices(self):
        return list(self.gdict.keys())

    def print_edges(self):
        edges = []
        for vertex in self.gdict:
            for next_vertex in self.gdict.get(vertex):
                if {vertex, next_vertex} not in edges:
                    edges.append({vertex, next_vertex})
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
            print(f"{vertex} added.")

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            if vertex2 not in self.gdict[vertex1]:
                self.gdict[vertex1].append(vertex2)
                print(f"{vertex2} added to {vertex1} vertex")
        else:
            self.gdict[vertex1] = [vertex2]
            print(f"New vertex {vertex1} and edge {vertex2} created")


graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = Graph(graph_elements)

print("Graph dictionary:")
print(g.print_dict())

print("Vertices:")
print(g.print_vertices())

print("Edges:")
print(g.print_edges())

print("Add Vertex:")
print(g.add_vertex("f"))
print(g.print_vertices())

print("Add Edge:")
print(g.add_edge({"a", "e"}))
print(g.add_edge({"a", "c"}))
print(g.print_edges())
print(g.print_dict())
