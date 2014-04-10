import unittest
from data_structures.radix_sort import radix_sort


class RadixSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty(self):
        input_li = []
        self.assertEquals(radix_sort(input_li, 10), input_li)

    def test_single(self):
        input_li = [1]
        self.assertEquals(radix_sort(input_li, 10), input_li)

    def test_ordered(self):
        input_li = [10, 21, 32, 43, 54, 65]
        expected = [10, 21, 32, 43, 54, 65]
        self.assertEquals(radix_sort(input_li, 10), expected)

    def test_sort(self):
        input_li = [65, 43, 21, 10, 32, 54]
        expected = [10, 21, 32, 43, 54, 65]
        self.assertEquals(radix_sort(input_li, 10), expected)

    def test_sort_neg(self):
        input_li = [-65, -43, -21, -10, -32, -54]
        expected = [-65, -54, -43, -32, -21, -10]
        self.assertEquals(radix_sort(input_li, 10), expected)

    def test_sort_mixed(self):
        input_li = [-65, 43, -21, -1, -32, -54, 101, -200, -3000]
        expected = [-3000, -200, -65, -54, -32, -21, -1, 43, 101]
        self.assertEquals(radix_sort(input_li, 10), expected)


if __name__ == '__main__':
    unittest.main()
