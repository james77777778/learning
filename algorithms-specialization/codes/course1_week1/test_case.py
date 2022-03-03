from karatsuba import multiply_karatsuba


def test_easy():
    n1 = "123"
    n2 = "456"

    assert multiply_karatsuba(n1, n2) == str(int(n1) * int(n2))


def test_hard():
    n1 = "1234567890123456789"
    n2 = "1234567890123456789"

    assert multiply_karatsuba(n1, n2) == str(int(n1) * int(n2))


def test_assignment():
    n1 = "3141592653589793238462643383279502884197169399375105820974944592"
    n2 = "2718281828459045235360287471352662497757247093699959574966967627"

    assert multiply_karatsuba(n1, n2) == str(int(n1) * int(n2))
