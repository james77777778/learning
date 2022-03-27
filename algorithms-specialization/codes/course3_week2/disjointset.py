from typing import List


class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0


class DisjointSet:  # with rank and path compression
    def __init__(self, elements):
        self.sets = {n: Node() for n in elements}
        self.count = len(self.sets)

    def find(self, element):
        n = self.sets[element]
        path_node: List[Node] = []
        while n.parent != n:
            n = n.parent
            path_node.append(n)  # 記錄路上的 nodes

        # path compression
        for v in path_node:
            v.parent = n
        return n

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            # 把 rank 小的掛到 rank 大的下方
            if u.rank < v.rank:
                u.parent = v
            else:
                v.parent = u
                if v.rank == u.rank:
                    u.rank += 1
            self.count -= 1

    def count_sets(self):
        return self.count
