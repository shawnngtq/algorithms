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
