from min_cut import read_adjacent_list, MinCutGraph


def test_easy():
    iterations = 5
    with open('test.txt', 'r') as f:
        raw_adjacent_list = read_adjacent_list(f)
    graph = MinCutGraph(raw_adjacent_list)

    min_cut = len(graph._get_all_distinct_edges(graph.adjacent_list))
    for _ in range(iterations):
        cut, _ = graph.mincut()
        min_cut = min(cut, min_cut)

    assert min_cut == 2


def test_assignment():
    answer = 17
    iterations = 200
    with open('kargerMinCut.txt', 'r') as f:
        raw_adjacent_list = read_adjacent_list(f)
    graph = MinCutGraph(raw_adjacent_list)

    min_cut = len(graph._get_all_distinct_edges(graph.adjacent_list))
    for _ in range(iterations):
        cut, _ = graph.mincut()
        min_cut = min(cut, min_cut)
        if min_cut == answer:  # early break
            break

    assert min_cut == 17
