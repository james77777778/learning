from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.adjacency_list = defaultdict(list)

    def add_edge(self, v: int, w: int):
        self.vertices.add(v)
        self.vertices.add(w)

        self.adjacency_list[v].append(w)

    def print_graph(self):
        for v in self.vertices:
            adj_nodes = self.adjacency_list[v]
            print(f'{v} -> {adj_nodes}')

    def reverse_graph(self) -> 'Graph':
        rev_g = Graph()
        for v, adj_nodes in self.adjacency_list.items():
            for w in adj_nodes:
                rev_g.add_edge(w, v)
        return rev_g


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 7)
    g.add_edge(7, 4)
    g.add_edge(4, 1)
    g.add_edge(7, 9)
    g.add_edge(9, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 9)
    g.add_edge(6, 8)
    g.add_edge(8, 2)
    g.add_edge(2, 5)
    g.add_edge(5, 8)

    print('Graph:')
    g.print_graph()

    print('Reversed Graph:')
    rev_g = g.reverse_graph()
    rev_g.print_graph()
