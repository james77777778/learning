import copy
import random
from typing import List, Tuple, Set

from heap import MinHeap


def parse_edges_and_vertices(path: str) -> Tuple[List[Tuple[int, int, int]], Set[int]]:
    vertices = set()
    edges = []
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


def insert_to_heap(
    target: int, min_heap: MinHeap, edges: List[Tuple[int, int, int]]
) -> Tuple[MinHeap, List[Tuple[int, int, int]]]:
    processed_edges = copy.deepcopy(edges)
    pop_idx = []
    for i, e in enumerate(edges):
        u, v, cost = e
        if target == u:
            min_heap.insert(cost, (u, v))
            pop_idx.append(i)
        if target == v:
            min_heap.insert(cost, (v, u))
            pop_idx.append(i)

    for i in reversed(pop_idx):
        processed_edges.pop(i)
    return min_heap, processed_edges


def compute_prim_mst_cost(edges: List[Tuple[int, int, int]], vertices: Set[int]) -> int:
    # init
    min_heap = MinHeap()
    init_vertex = random.choice(tuple(vertices))
    processed_vertices = set()  # X
    processed_vertices.add(init_vertex)
    min_heap, edges = insert_to_heap(init_vertex, min_heap, edges)
    mini_spanning_tree = list()  # T
    res = 0

    while len(processed_vertices) != len(vertices):
        cost, (u, v) = min_heap.extract_min()
        while v in processed_vertices:
            cost, (u, v) = min_heap.extract_min()
        res += cost
        mini_spanning_tree.append((u, v))
        processed_vertices.add(v)
        min_heap, edges = insert_to_heap(v, min_heap, edges)

    return res


if __name__ == '__main__':
    edges, vertices = parse_edges_and_vertices('edges.txt')
    res = compute_prim_mst_cost(edges, vertices)
    print(f'Overall cost of MST: {res}')
