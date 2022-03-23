from scheduling import parse_jobs, compute_sum_by_difference, compute_sum_by_ratio
from prim_mst import parse_edges_and_vertices, compute_prim_mst_cost


def test_scheduling_difference():
    jobs = parse_jobs('jobs.txt')

    res = compute_sum_by_difference(jobs)

    assert res == 69119377652


def test_scheduling_ratio():
    jobs = parse_jobs('jobs.txt')

    res = compute_sum_by_ratio(jobs)

    assert res == 67311454237


def test_prim_mst():
    edges, vertices = parse_edges_and_vertices('edges.txt')

    res = compute_prim_mst_cost(edges, vertices)

    assert res == -3612829
