#! /usr/bin/env python

import unittest
import queue


class EnqueueTests(unittest.TestCase):

    def setUp(self):
        self.testloop = [True, 6, 'this', [1, "a", True], {'this': 'that'}]

    def test_types(self):
        for i in self.testloop:
            self.qtest = queue.Queue()
            self.qtest.enqueue(i)
            self.assertEqual(self.qtest.head.value, i)


class DequeueTests(unittest.TestCase):

    def setUp(self):
        self.qtest = queue.Queue()
        for i in [True, 6, 'this']:
            self.qtest.enqueue(i)

    def test_dequeue(self):
        self.assertEqual(self.qtest.dequeue(), True)

    def test_dequeue_head(self):
        self.qtest.dequeue()
        self.assertEqual(self.qtest.head.value, 6)

    def test_dequeue_empty(self):
        self.qtest.dequeue()
        self.qtest.dequeue()
        self.qtest.dequeue()
        self.assertRaises(self.qtest.dequeue)

    def test_dequeue_value(self):
        self.qtest.dequeue()
        self.qtest.dequeue()
        self.qtest.dequeue()
        self.assertEqual(self.qtest.tail, None)


class LengthTests(unittest.TestCase):

    def setUp(self):
        self.qtest = queue.Queue()

    def test_length(self):
        self.qtest.enqueue(6)
        self.assertEquals(self.qtest.length, 1)

    def test_length_empty(self):
        self.assertEqual(self.qtest.length, 0)


if __name__ == '__main__':
    unittest.main()
