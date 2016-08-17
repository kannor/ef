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


def find():
    pass


def compact():
    pass
