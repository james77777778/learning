from collections import defaultdict


class WeightedDirectedGraph:
    def __init__(self):
        self.vertices = set()
        self.adjacency_list = defaultdict(list)

    def add_edge(self, v: int, w: int, weight: int):
        self.vertices.add(v)
        self.vertices.add(w)

        self.adjacency_list[v].append((w, weight))

    def print_graph(self):
        for v in self.vertices:
            adj_nodes_with_weight = self.adjacency_list[v]
            print(f'{v} -> {adj_nodes_with_weight}')


if __name__ == '__main__':
    g = WeightedDirectedGraph()
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 4)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 6)
    g.add_edge(3, 4, 3)

    print('WeightedDirectedGraph:')
    print('ex: s -> [(v1, v1 weight), ...]')
    print()
    g.print_graph()
