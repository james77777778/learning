import math
from typing import Tuple


def get_components(number: str) -> Tuple[str, str]:
    half_n = len(number) // 2
    c1 = number[:half_n]
    c2 = number[half_n:]

    return c1, c2


def get_len_max(len_n1, len_n2) -> int:
    max_len = max(len_n1, len_n2)
    log_max_len = math.log2(max_len)
    if math.floor(log_max_len) != log_max_len:
        max_len = int(2 ** math.ceil(log_max_len))
    return max_len


def pad_zero_digits(n1: str, n2: str, max_len: int) -> Tuple[str, str]:
    n2 = "0" * (max_len - len(n2)) + n2
    n1 = "0" * (max_len - len(n1)) + n1
    return n1, n2


def multiply_karatsuba(n1: str, n2: str) -> str:
    if int(n1) < 10 or int(n2) < 10:
        res = int(n1) * int(n2)
        return str(res)

    # pad zeros to n1 or n2 if
    # 1. the digits of n1, n2 are not the same
    # 2. the digits is not equal to the exponential of 2
    max_len = get_len_max(len(n1), len(n2))
    n1, n2 = pad_zero_digits(n1, n2, max_len)

    # get components
    a, b = get_components(n1)
    c, d = get_components(n2)

    # compute a*c
    ac = multiply_karatsuba(a, c)

    # compute b*d
    bd = multiply_karatsuba(b, d)

    # compute (a+b)*(c+d)
    x = int(a) + int(b)
    y = int(c) + int(d)
    xy = multiply_karatsuba(str(x), str(y))

    # gauss's trick a*d+b*c
    int_ad_add_bc = int(xy) - int(ac) - int(bd)

    final_res = int(ac) * pow(10, max_len) + int_ad_add_bc * pow(10, max_len // 2) + int(bd)
    return str(final_res)


if __name__ == "__main__":
    n1 = "3141592653589793238462643383279502884197169399375105820974944592"
    n2 = "2718281828459045235360287471352662497757247093699959574966967627"

    res = multiply_karatsuba(n1, n2)
    print(res)
