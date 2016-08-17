import unittest

from functions.functions import rotate, lcm, find, compact


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

        l = [330, 65, 15]
        self.assertEqual(lcm(l), 4290)
        l.reverse()
        self.assertEqual(lcm(l), 4290)

        d = zip([[12, 30], [24, 300]], [60, 600])
        for i in d:
            self.assertEqual(lcm(i[0]), i[-1])

    def test_find(self):
        pass

    def test_compact(self):

        # Requested test case
        l = [1, 3, 7, 7, 8, 9, 9, 9, 10]
        self.assertEqual(compact(l), [1, 3, 7, 8, 9, 10])
