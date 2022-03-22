from typing import List, Tuple


def parse_jobs(path: str) -> List[Tuple[int, int]]:
    jobs = []
    with open(path, 'r') as f:
        for line in f:
            data = line.strip().split(' ')
            if len(data) < 2:
                continue
            weight, length = int(data[0]), int(data[1])
            jobs.append((weight, length))
    return jobs


def compute_sum_by_difference(jobs: List[Tuple[int, int]]) -> int:
    greedy_scores_with_weights = [((weight - length), weight) for weight, length in jobs]
    sort_indices = [
        x for x, _ in sorted(enumerate(greedy_scores_with_weights), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    ]

    res = 0
    now_time = 0
    for ind in sort_indices:
        weight, length = jobs[ind]
        now_time += length
        res += weight * now_time

    return res


def compute_sum_by_ratio(jobs: List[Tuple[int, int]]) -> int:
    greedy_scores_with_weights = [weight / length for weight, length in jobs]
    sort_indices = [
        x for x, _ in sorted(enumerate(greedy_scores_with_weights), key=lambda x: x[1], reverse=True)
    ]

    res = 0
    now_time = 0
    for ind in sort_indices:
        weight, length = jobs[ind]
        now_time += length
        res += weight * now_time

    return res


if __name__ == '__main__':
    # easy problem
    jobs = [(3, 5), (1, 2)]
    res = compute_sum_by_difference(jobs)
    print(f'(Easy, difference)       The sum of weighted completion time: {res}')
    res = compute_sum_by_ratio(jobs)
    print(f'(Easy, ratio)            The sum of weighted completion time: {res}')

    # assignment
    jobs = parse_jobs('jobs.txt')
    res = compute_sum_by_difference(jobs)
    print(f'(Assignment, difference) The sum of weighted completion time: {res}')
    res = compute_sum_by_ratio(jobs)
    print(f'(Assignment, ratio)      The sum of weighted completion time: {res}')
