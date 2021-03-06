import functools
try:
    from math import gcd
except ImportError:
    from fractions import gcd


def rotate(seq, n):
    """
    Rotate <seq> <n> steps to the right.  If n is negative, rotates left

    Args:
        seq: iterable
        n: steps
    Returns:
        Rotated <seq> <n> steps
    """

    return seq[-n:] + seq[:-n]


def lcm(seq):
    """
    Least common multiple of <seq> entries.

    Args:
        seq: int iterable
    Returns:
        LCM of <seq>
    """

    def _gcd(a, b):
        # returns greatest common divisor of a and b
        if(b or a) < 0:
            return -gcd(a, b)
        return gcd(a, b)

    return abs(functools.reduce(lambda a, b: (a * b) // _gcd(a, b), seq))


def find_char_nn(str1, str2):
    """
    Inersection of str1 and str2 with O(N*N)

    Args:'
        str1: String
        str2: String
    Returns:
        Inersection of str1 and str2 else ''
    """

    results = []
    for char in str1:
        for _char in str2:
            if char == _char:
                results.append(char)
                break

    return ''.join(results)


def find_car_n(str1, str2):
    """
    Inersection of str1 and str2 with O(N)

    Args:'
        str1: String
        str2: String
    Returns:
        Inersection of str1 and str2 else ''
    """

    results = []
    seen = set(str2)
    for char in str1:
        if char in seen:
            results.append(char)

    return ''.join(results)


def compact(seq):
    """
    Unique enties of a sotred array.

    Args:
        seq: sorted array
    """

    new = []
    for it in seq:
        if it not in new:
            new.append(it)

    return new
