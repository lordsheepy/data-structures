import unittest
from data_structures.insertion_sort import insertion_sort


class InsertionSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty(self):
        input_l = []
        self.assertEquals(insertion_sort(input_l), input_l)

    def test_single(self):
        input_l = [1]
        self.assertEquals(insertion_sort(input_l), input_l)

    def test_ordered(self):
        input_l = [1, 2, 3, 4, 5, 6]
        self.assertEquals(insertion_sort(input_l), input_l)

    def test_sort(self):
        input_l = [6, 4, 2, 1, 3, 5]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEquals(insertion_sort(input_l), expected)


if __name__ == '__main__':
    unittest.main()
