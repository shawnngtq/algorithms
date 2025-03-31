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

    def add_matrix_edge(self, edge):
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
    "e": ["d"],
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
print(g.add_matrix_edge({"a", "e"}))
print(g.add_matrix_edge({"a", "c"}))
print(g.print_edges())
print(g.print_dict())


class Graph:
    """
    Reference
    ---------
    https://www.geeksforgeeks.org/introduction-to-graphs-data-structure-and-algorithm-tutorials/
    """

    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.matrix = [[0] * number_of_vertices for i in range(number_of_vertices)]
        self.list = [[] for _ in range(number_of_vertices)]

    def can_create_edge(self, i, j):
        if i >= self.number_of_vertices or j >= self.number_of_vertices:
            print("Vertex don't exist")
            return False
        if i == j:
            print("Vertex can't connect itself")
            return False
        return True

    def add_matrix_edge(self, i, j):
        if self.can_create_edge(i, j):
            self.matrix[i][j] = 1
            self.matrix[j][i] = 1

    def add_matrix_vertex(self):
        self.number_of_vertices += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.number_of_vertices)

    def display_adjacent_matrix(self):
        print("Adjacent Matrix")
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def add_list_edge(self, i, j):
        if self.can_create_edge(i, j):
            self.list[i].append(j)
            self.list[j].append(i)

    def add_list_vertex(self):
        self.number_of_vertices += 1
        self.list.append([])

    def display_adjacent_list(self):
        print("Adjacent List")
        for i, row in enumerate(self.list):
            print(f"{i}: {" ".join(map(str, row))}")


matrix = Graph(4)
matrix.add_matrix_edge(0, 1)
matrix.add_matrix_edge(0, 2)
matrix.add_matrix_edge(1, 2)
matrix.add_matrix_edge(2, 3)
matrix.add_matrix_vertex()
matrix.display_adjacent_matrix()
matrix.add_list_edge(0, 1)
matrix.add_list_edge(0, 2)
matrix.add_list_edge(1, 2)
matrix.add_list_edge(2, 3)
matrix.add_list_vertex()
matrix.display_adjacent_list()


# list of edges
# adjacentlist
# adjacentmatrix


class GraphAdjacentList:
    def __init__(self) -> None:
        self.adjacent_list = {}
        self.number_of_nodes = 0

    def __repr__(self) -> str:
        return str(self.adjacent_list)

    def print_number_of_nodes(self):
        return self.number_of_nodes

    def add_node(self, node):
        if node in self.adjacent_list:
            return "No duplicated nodes"
        else:
            self.number_of_nodes += 1
            self.adjacent_list[node] = []
            return self

    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)
        return self

    def remove_edge(self, node1, node2):
        self.adjacent_list[node1].remove(node2)
        self.adjacent_list[node2].remove(node1)
        return self


graph = GraphAdjacentList()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_edge(0, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 2)
graph.add_edge(3, 1)
graph.add_edge(3, 4)
graph.add_edge(4, 2)
graph.add_edge(4, 5)
graph.add_edge(6, 0)
print(graph)
graph.remove_edge(0, 6)
print(graph)
