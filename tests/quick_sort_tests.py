import unittest
from data_structures.quick_sort import quick_sort, pivot


class QuickSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty(self):
        input_li = []
        self.assertEquals(quick_sort(input_li), input_li)

    def test_single(self):
        input_li = [1]
        self.assertEquals(quick_sort(input_li), input_li)

    def test_ordered(self):
        input_li = [1, 2, 3, 4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEquals(quick_sort(input_li), expected)

    def test_sort(self):
        input_li = [6, 4, 2, 1, 3, 5]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEquals(quick_sort(input_li), expected)


class PivotTests(unittest.TestCase):

    def setUp(self):
        self.inp = [6, 4, 2, 1, 3, 5]

    def tearDown(self):
        pass

    def test_front_pivot(self):
        self.assertEquals(pivot(self.inp, method='first'), 6)

    def test_last_pivot(self):
        self.assertEquals(pivot(self.inp, method='last'), 5)

    def test_median_pivot(self):
        self.assertEquals(pivot(self.inp, method='median'), 5)


if __name__ == '__main__':
    unittest.main()
