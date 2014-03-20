import unittest
from data_structures.merge_sort import merge_sort


class MergeSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty(self):
        input_li = []
        self.assertEquals(merge_sort(input_li), input_li)

    def test_single(self):
        input_li = [1]
        self.assertEquals(merge_sort(input_li), input_li)

    def test_ordered(self):
        input_li = [1, 2, 3, 4, 5, 6]
        self.assertEquals(merge_sort(input_li), input_li)

    def test_sort(self):
        input_li = [6, 4, 2, 1, 3, 5]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEquals(merge_sort(input_li), expected)


if __name__ == '__main__':
    unittest.main()
