from typing import Tuple, List


def merge_and_count_split_inversion(arr1, arr2) -> Tuple[List[int], int]:
    n_inversions = 0
    sorted_arr = []
    idx_arr1, idx_arr2 = 0, 0

    while idx_arr1 < len(arr1) and idx_arr2 < len(arr2):
        if arr1[idx_arr1] < arr2[idx_arr2]:
            sorted_arr.append(arr1[idx_arr1])
            idx_arr1 += 1
        else:
            sorted_arr.append(arr2[idx_arr2])
            idx_arr2 += 1
            # count inversions
            n_inversions += len(arr1) - idx_arr1

    while idx_arr1 < len(arr1):
        sorted_arr.append(arr1[idx_arr1])
        idx_arr1 += 1

    while idx_arr2 < len(arr2):
        sorted_arr.append(arr2[idx_arr2])
        idx_arr2 += 1

    return sorted_arr, n_inversions


def sort_and_count_inversion(arr, n) -> Tuple[List[int], int]:
    if n == 1:
        return arr, 0

    # compute mid
    half_n = len(arr) // 2

    # 1st half of arr
    b_arr, x = sort_and_count_inversion(arr[:half_n], half_n)

    # 2nd half of arr
    c_arr, y = sort_and_count_inversion(arr[half_n:], len(arr) - half_n)

    # count split inversion
    d_arr, z = merge_and_count_split_inversion(b_arr, c_arr)

    return d_arr, x + y + z


if __name__ == '__main__':
    arr = []
    with open('IntegerArray.txt', 'r') as f:
        for line in f:
            if line.strip().isdecimal():
                arr.append(int(line))
    sorted_arr, n_inversions = sort_and_count_inversion(arr, len(arr))
    print(n_inversions)
