from .graph import WeightedDirectedGraph
from .dijkstra import dijkstra_shortest_path


def test_easy():
    g = WeightedDirectedGraph()
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 4)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 6)
    g.add_edge(3, 4, 3)

    source_vertex = 1
    a, b = dijkstra_shortest_path(g, source_vertex)

    assert a == {1: 0, 2: 1, 3: 3, 4: 6}
    assert b == {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4]}


def test_assignment():
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
    a, _ = dijkstra_shortest_path(g, source_vertex)
    targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    res = [str(a[t]) for t in targets]
    res_string = ','.join(res)

    assert res_string == '2599,2610,2947,2052,2367,2399,2029,2442,2505,3068'
