#! /usr/bin/env python

import unittest
import stack


class StackTest(unittest.TestCase):

    def test_push(self):
        bob = stack.Stack()
        bob.push('this')
        self.assertEqual(bob.head.value, 'this')

    def test_head(self):
        bob = stack.Stack()
        self.assertFalse(bob.head)

    def test_push_next(self):
        bob = stack.Stack()
        bob.push('this')
        bob.push('that')
        self.assertEqual(bob.head.next.value, 'this')


class PopTest(unittest.TestCase):

    def setUp(self):
        self.bob = stack.Stack()

    def test_pop_none(self):
        self.assertRaises(self.bob.pop)

    def test_pop_one(self):
        self.bob.push('This')
        self.assertEqual(self.bob.pop(), 'This')

    def test_pop_next(self):
        self.bob.push('This')
        self.bob.push('That')
        self.bob.push('theother')
        self.bob.pop()
        self.assertEqual(self.bob.head.next.value, 'This')

if __name__ == "__main__":
    unittest.main()
