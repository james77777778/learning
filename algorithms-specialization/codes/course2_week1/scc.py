from typing import List

from graph import Graph


def get_finishing_order_by_dfs(g: Graph) -> List[int]:
    # init
    t = 0
    vertices = g.vertices
    explored = set()
    finishing = list()

    # dfs
    for v in vertices:
        if v in explored:
            continue

        dfs_stack = list()
        dfs_stack.append(v)
        explored.add(v)
        while len(dfs_stack) > 0:
            vertex = dfs_stack[-1]
            not_visit = True
            for adj_node in g.adjacency_list[vertex]:
                if adj_node in explored:
                    continue
                dfs_stack.append(adj_node)
                explored.add(adj_node)
                not_visit = False
                break
            if not_visit:
                dfs_stack.pop()
                t += 1
                finishing.append(vertex)
    return finishing


def get_sccs_by_dfs(g: Graph, finishing_order: List[int]) -> List[List[int]]:
    # init
    explored = set()
    sccs = list()

    # dfs
    for v in reversed(finishing_order):
        if v in explored:
            continue
        scc = [v]
        dfs_stack = list()
        dfs_stack.append(v)
        explored.add(v)
        while len(dfs_stack) > 0:
            vertex = dfs_stack[-1]
            not_visit = True
            for adj_node in g.adjacency_list[vertex]:
                if adj_node in explored:
                    continue
                scc.append(adj_node)
                dfs_stack.append(adj_node)
                explored.add(adj_node)
                not_visit = False
                break
            if not_visit:
                dfs_stack.pop()
        sccs.append(scc)
    return sccs


def compute_sccs(g: Graph) -> List[List[int]]:
    grev = g.reverse_graph()
    finishing_order = get_finishing_order_by_dfs(grev)
    sccs = get_sccs_by_dfs(g, finishing_order)
    return sccs


def get_sorted_size_of_sccs(sccs: List[List[int]]):
    sccs_sizes = [len(scc) for scc in sccs]
    sccs_sizes = sorted(sccs_sizes, reverse=True)
    return sccs_sizes[:5]


if __name__ == "__main__":
    # sample graph
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
    print(sccs)
    print(f"size of 5 largest scc: {sccs_sizes}")

    # assignment
    g = Graph()
    with open("SCC.txt", "r") as f:
        for line in f:
            edge = line.strip().split(" ")
            edge = [int(n) for n in edge]
            v, w = edge
            g.add_edge(v, w)

    sccs = compute_sccs(g)
    sccs_sizes = get_sorted_size_of_sccs(sccs)

    print(f"size of 5 largest scc: {sccs_sizes}")
