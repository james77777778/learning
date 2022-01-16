from inversion import sort_and_count_inversion


def test_easy():
    arr = [1, 3, 5, 2, 4, 6]
    sorted_arr, n_inversions = sort_and_count_inversion(arr, len(arr))

    assert n_inversions == 3


def test_assignment():
    arr = []
    with open('IntegerArray.txt', 'r') as f:
        for line in f:
            if line.strip().isdecimal():
                arr.append(int(line))
    sorted_arr, n_inversions = sort_and_count_inversion(arr, len(arr))

    assert n_inversions == 2407905288
