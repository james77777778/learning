from typing import Tuple

from .graph import WeightedDirectedGraph


INF_DISTANCE = 1000000


def brute_force_greedy_function(g: WeightedDirectedGraph, a: dict, x: set) -> Tuple[int, int, int]:
    min_edge = (None, None, INF_DISTANCE)  # (v, w, A[v] + l_vw)
    for v in x:
        for adj_node_with_weight in g.adjacency_list[v]:
            w, weight = adj_node_with_weight
            if w in x:
                continue
            if a[v] + weight < min_edge[2]:
                min_edge = (v, w, a[v] + weight)
    return min_edge


def dijkstra_shortest_path(g: WeightedDirectedGraph, source: int):
    x = set()  # vertices processed so far
    x.add(source)
    a = {source: 0}  # computed shortest path distance
    b = {source: [source]}  # computed shortest path

    while len(x) != len(g.vertices):
        min_edge = brute_force_greedy_function(g, a, x)
        if min_edge[0] is None:
            break
        v, w, greedy_score = min_edge
        x.add(w)
        a[w] = greedy_score
        b[w] = b[v] + [w]

    for v in g.vertices:
        if v in x:
            continue
        a[v] = INF_DISTANCE
        b[v] = []

    return a, b


if __name__ == '__main__':
    # sample graph
    g = WeightedDirectedGraph()
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 4)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 6)
    g.add_edge(3, 4, 3)

    source_vertex = 1
    a, b = dijkstra_shortest_path(g, source_vertex)
    print(a)
    print(b)

    # assignment
    g = WeightedDirectedGraph()
    with open('dijkstraData.txt', 'r') as f:
        for line in f:
            data = line.strip().split('\t')
            v = int(data[0])
            for adj in data[1:]:
                w, weight = adj.split(',')
                w, weight = int(w), int(weight)
                g.add_edge(v, w, weight)

    source_vertex = 1
    a, b = dijkstra_shortest_path(g, source_vertex)

    targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    print(f'Targets: {targets}')
    print('Assignment result:')
    res = [str(a[t]) for t in targets]
    print(','.join(res))

    for t in targets:
        print(b[t])
