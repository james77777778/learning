from typing import List, Tuple, Set

from disjointset import DisjointSet


def parse_edges(path: str) -> Tuple[List[Tuple[int, int, int]], Set[int]]:
    edges = []
    vertices = set()
    with open(path, 'r') as f:
        for line in f:
            data = line.strip().split(' ')
            if len(data) < 3:
                continue
            u, v, cost = int(data[0]), int(data[1]), int(data[2])
            edges.append((u, v, cost))
            vertices.add(u)
            vertices.add(v)
    return edges, vertices


def kclustering(edges: List[Tuple[int, int, int]], vertices: Set[int], k: int):
    # sort edges in order of increasing cost
    edges = sorted(edges, key=lambda x: x[2])

    # init disjoint set
    disjoint_set = DisjointSet(vertices)

    for data in edges:
        u, v, cost = data

        if disjoint_set.count_sets() == 4:  # stop to union
            u_parent = disjoint_set.find(u)
            v_parent = disjoint_set.find(v)
            if u_parent != v_parent:
                return cost
        else:
            disjoint_set.union(u, v)

    return StopIteration(f'No sufficent vertices of {k}-clustering')


if __name__ == '__main__':
    edges, vertices = parse_edges('clustering1.txt')
    ans = kclustering(edges, vertices, k=4)
    print(f'Maximum spacing: {ans}')
