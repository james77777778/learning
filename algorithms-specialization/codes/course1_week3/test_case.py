from .quick_sort import quick_sort_with_first_pivot, quick_sort_with_last_pivot, quick_sort_with_median_of_three_pivot


def test_easy():
    arr = [3, 2, 8, 5, 1, 4, 7, 6]
    sorted_arr, num_comp = quick_sort_with_first_pivot(arr, len(arr), 0)

    assert sorted_arr == [1, 2, 3, 4, 5, 6, 7, 8]
    assert num_comp == 15


def test_assignment_1():
    arr = []
    with open("QuickSort.txt", "r") as f:
        for line in f:
            if len(line.strip()) < 1:
                continue
            arr.append(int(line.strip()))

    arr, num_comp = quick_sort_with_first_pivot(arr, len(arr), 0)

    assert num_comp == 162085


def test_assignment_2():
    arr = []
    with open("QuickSort.txt", "r") as f:
        for line in f:
            if len(line.strip()) < 1:
                continue
            arr.append(int(line.strip()))

    arr, num_comp = quick_sort_with_last_pivot(arr, len(arr), 0)

    assert num_comp == 164123


def test_assignment_3():
    arr = []
    with open("QuickSort.txt", "r") as f:
        for line in f:
            if len(line.strip()) < 1:
                continue
            arr.append(int(line.strip()))

    arr, num_comp = quick_sort_with_median_of_three_pivot(arr, len(arr), 0)

    assert num_comp == 138382
