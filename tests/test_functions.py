import random
import unittest

from functions.functions import (
    rotate, lcm, compact, find_char_nn, find_car_n)


class FunctionsTestCase(unittest.TestCase):

    def test_rotate(self):
        # Reuested test case
        l = [1, 2, 3, 4, 5, 6]
        self.assertEqual(rotate(l, 2), [5, 6, 1, 2, 3, 4])

        # Other test
        l = tuple('abcde')
        n = len(l)

        r = rotate(l, 1)
        self.assertEqual(''.join(r), 'eabcd')

        r = rotate(l, -1)
        self.assertEqual(''.join(r), 'bcdea')

        for i in range(n):
            e = l
            d = rotate(l, i)
            for j in range(i):
                e = rotate(e, 1)
            self.assertEqual(tuple(d), tuple(e))
            d = rotate(d, -i)
            self.assertEqual(tuple(d), l)
            e = rotate(e, n - i)
            self.assertEqual(tuple(e), l)

        for i in range(n):
            e = l
            d = rotate(l, -i)
            for j in range(i):
                e = rotate(e, -1)
            self.assertEqual(tuple(d), tuple(e))
            d = rotate(d, i)
            self.assertEqual(tuple(d), l)
            e = rotate(e, i - n)
            self.assertEqual(tuple(e), l)

    def test_lcm(self):

        # Requested test case
        l = [3, 4]
        self.assertEqual(lcm(l), 12)

        # Others
        l = [330, 65, 15]
        self.assertEqual(lcm(l), 4290)
        l.reverse()
        self.assertEqual(lcm(l), 4290)

        d = zip([[12, 30], [24, 300]], [60, 600])
        for i in d:
            self.assertEqual(lcm(i[0]), i[-1])

    def test_find(self):
        string1 = "if I'm playing with a sorting function and observe function"
        string2 = "I need to look at what the algorithm is doing in case."

        self.assertEqual(find_char_nn(string1, string2),
                         find_car_n(string1, string2))

    def test_compact(self):

        # Requested test case
        l = [1, 3, 7, 7, 8, 9, 9, 9, 10]
        self.assertEqual(compact(l), [1, 3, 7, 8, 9, 10])

        n = len(l)

        # Others
        l = sorted([1, 2, 3, 1, 4, 5, 5, 2, 3, 9, 10, 11, 3, 10, 9, 0, 7])
        self.assertEqual(compact(l), list(sorted(set(l))))

        for i in range(n):
            l = random.sample(range(100), i)
            l = sorted(l)
            self.assertEqual(compact(l), list(sorted(set(l))))

if __name__ == "__main__":
    unittest.main()
