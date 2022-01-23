from typing import List, Tuple


def choose_first_as_pivot(arr, n) -> Tuple[int, int]:
    return arr[0], 0


def choose_last_as_pivot(arr, n) -> Tuple[int, int]:
    return arr[-1], n - 1


def choose_median_of_three_as_pivot(arr, n) -> Tuple[int, int]:
    # get middle idx
    if n / 2 > n // 2:
        middle = n // 2
    else:
        middle = n // 2 - 1

    # find median of three
    a, b, c = arr[0], arr[middle], arr[-1]
    if a > b:
        if a < c:
            return a, 0
        elif b > c:
            return b, middle
        else:  # a > c, b < c or b < c, a > c
            return c, n - 1
    else:  # a < b
        if a > c:
            return a, 0
        elif b < c:
            return b, middle
        else:
            return c, n - 1


def partition(arr, pivot, idx_pivot) -> Tuple[List[int], int]:
    # swap pivot with first element
    arr[0], arr[idx_pivot] = arr[idx_pivot], arr[0]

    # init
    idx_less = 1

    # loop
    for idx_cur in range(1, len(arr)):
        if arr[idx_cur] < pivot:
            arr[idx_cur], arr[idx_less] = arr[idx_less], arr[idx_cur]
            idx_less += 1
    idx_less -= 1

    # swap pivot to the right place
    arr[0], arr[idx_less] = arr[idx_less], arr[0]

    return arr, idx_less


def quick_sort_with_first_pivot(arr, n, comp_count) -> Tuple[List[int], int]:
    if n <= 1:
        return arr, 0

    pivot, idx_pivot = choose_first_as_pivot(arr, n)
    arr, new_idx_pivot = partition(arr, pivot, idx_pivot)

    arr[:new_idx_pivot], left = quick_sort_with_first_pivot(arr[:new_idx_pivot], len(arr[:new_idx_pivot]), comp_count)
    arr[new_idx_pivot + 1:], right = quick_sort_with_first_pivot(arr[new_idx_pivot + 1:], len(arr[new_idx_pivot + 1:]), comp_count)

    return arr, n - 1 + left + right  # at this level: n - 1 (without pivot) and add two subarray results


def quick_sort_with_last_pivot(arr, n, comp_count) -> Tuple[List[int], int]:
    if n <= 1:
        return arr, 0

    pivot, idx_pivot = choose_last_as_pivot(arr, n)
    arr, new_idx_pivot = partition(arr, pivot, idx_pivot)

    arr[:new_idx_pivot], left = quick_sort_with_last_pivot(arr[:new_idx_pivot], len(arr[:new_idx_pivot]), comp_count)
    arr[new_idx_pivot + 1:], right = quick_sort_with_last_pivot(arr[new_idx_pivot + 1:], len(arr[new_idx_pivot + 1:]), comp_count)

    return arr, n - 1 + left + right  # at this level: n - 1 (without pivot) and add two subarray results


def quick_sort_with_median_of_three_pivot(arr, n, comp_count) -> Tuple[List[int], int]:
    if n <= 1:
        return arr, 0

    pivot, idx_pivot = choose_median_of_three_as_pivot(arr, n)
    arr, new_idx_pivot = partition(arr, pivot, idx_pivot)

    arr[:new_idx_pivot], left = quick_sort_with_median_of_three_pivot(arr[:new_idx_pivot], len(arr[:new_idx_pivot]), comp_count)
    arr[new_idx_pivot + 1:], right = quick_sort_with_median_of_three_pivot(arr[new_idx_pivot + 1:], len(arr[new_idx_pivot + 1:]), comp_count)

    return arr, n - 1 + left + right  # at this level: n - 1 (without pivot) and add two subarray results


if __name__ == '__main__':
    arr = [3, 2, 8, 5, 1, 4, 7, 6]
    print(arr)
    arr, num_comp = quick_sort_with_first_pivot(arr, len(arr), 0)
    print(arr)
    print(num_comp)

    # assignment 1
    arr = []
    with open('QuickSort.txt', 'r') as f:
        for line in f:
            if len(line.strip()) < 1:
                continue
            arr.append(int(line.strip()))

    arr, num_comp = quick_sort_with_first_pivot(arr, len(arr), 0)
    print(f'first {num_comp}')

    # assignment 2
    arr = []
    with open('QuickSort.txt', 'r') as f:
        for line in f:
            if len(line.strip()) < 1:
                continue
            arr.append(int(line.strip()))

    arr, num_comp = quick_sort_with_last_pivot(arr, len(arr), 0)
    print(f'last {num_comp}')

    # assignment 3
    arr = []
    with open('QuickSort.txt', 'r') as f:
        for line in f:
            if len(line.strip()) < 1:
                continue
            arr.append(int(line.strip()))

    arr, num_comp = quick_sort_with_median_of_three_pivot(arr, len(arr), 0)
    print(f'median of three {num_comp}')
