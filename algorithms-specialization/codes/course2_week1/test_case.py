from .graph import Graph
from .scc import compute_sccs, get_sorted_size_of_sccs


def test_easy():
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

    sccs = compute_sccs(g)
    sccs_sizes = get_sorted_size_of_sccs(sccs)

    assert sccs_sizes == [3, 3, 3]


def test_assignment():
    g = Graph()
    with open("SCC.txt", "r") as f:
        for line in f:
            edge = line.strip().split(" ")
            edge = [int(n) for n in edge]
            v, w = edge
            g.add_edge(v, w)

    sccs = compute_sccs(g)
    sccs_sizes = get_sorted_size_of_sccs(sccs)

    assert sccs_sizes == [434821, 968, 459, 313, 211]
