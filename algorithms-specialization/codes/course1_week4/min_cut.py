import copy
import random
from io import TextIOWrapper
from typing import List, Dict, Tuple


def read_adjacent_list(f: TextIOWrapper) -> List[int]:
    res = []
    for line in f:
        nodes = line.strip().split()
        nodes = [int(n) for n in nodes]
        res.append(nodes)
    return res


class MinCutGraph:
    def __init__(self, input_list: List[int]):
        self.adjacent_list = self._parse_graph(input_list)

    def _parse_graph(self, input_list: List[int]) -> Dict:
        res = {}
        for line in input_list:
            node, adjacent_nodes = line[0], line[1:]
            res[node] = adjacent_nodes
        return res

    def _get_all_distinct_edges(self, cur_adjacent_list: Dict[int, List[int]]) -> List[Tuple[int, int]]:
        edges = []
        for k, adj_list in cur_adjacent_list.items():
            for adj in adj_list:
                if adj != k:
                    edges.append((k, adj))
        return edges

    def _contract(self, cur_adjacent_list: Dict[int, List[int]], chosen_edge) -> Dict:
        u, v = chosen_edge
        # merge
        cur_adjacent_list[u] = cur_adjacent_list[u] + cur_adjacent_list.pop(v)

        # relabel (v mapping to u)
        for k, adj_list in cur_adjacent_list.items():
            adj_list = [adj if adj != v else u for adj in adj_list]
            cur_adjacent_list[k] = adj_list

        return cur_adjacent_list

    def _remove_selfloops(self, cur_adjacent_list: Dict[int, List[int]]) -> Dict:
        for k, adj_list in cur_adjacent_list.items():
            adj_list = [adj for adj in adj_list if adj != k]
            cur_adjacent_list[k] = adj_list
        return cur_adjacent_list

    def print_graph(self):
        nodes = self.adjacent_list.keys()
        nodes = sorted(nodes)
        for n in nodes:
            print(f"{n}: {self.adjacent_list[n]}")

    def mincut(self, random_seed: int = None) -> int:
        if random_seed:
            random.seed(random_seed)
        # init
        cur_adjacent_list = copy.deepcopy(self.adjacent_list)

        while len(cur_adjacent_list) > 2:
            # random pick edge
            all_edges = self._get_all_distinct_edges(cur_adjacent_list)
            choesn_edge = random.choice(all_edges)

            # contract u & v into a single vertex
            cur_adjacent_list = self._contract(cur_adjacent_list, choesn_edge)

            # remove self-loops
            cur_adjacent_list = self._remove_selfloops(cur_adjacent_list)

        # output mincut value
        for k, v in cur_adjacent_list.items():
            return len(v), cur_adjacent_list.keys()


if __name__ == "__main__":
    iterations = 100

    with open("kargerMinCut.txt", "r") as f:
        raw_adjacent_list = read_adjacent_list(f)

    graph = MinCutGraph(raw_adjacent_list)

    min_cut = len(graph._get_all_distinct_edges(graph.adjacent_list))
    for idx in range(iterations):
        cut, super_vertices = graph.mincut()
        print(f"Index: {idx: <4}, Cut: {cut: <5}, Super Vertices: {super_vertices}, Min Cut: {min_cut}")
        min_cut = min(cut, min_cut)
    print(min_cut)
