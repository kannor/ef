import unittest

from functions.functions import rotate, lcm, find, compact


class FunctionsTestCase(unittest.TestCase):

    def test_rotate(self):
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
        pass

    def test_find(self):
        pass

    def test_compact(self):
        pass
