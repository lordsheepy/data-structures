import unittest
from binarytree import BinaryTree as Tree


class BinaryTreeTests(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(7)

    def test_insert(self):
        self.tree.insert(9)
        self.assertTrue(self.tree.contains(9))

    def test_reinsert(self):
        self.tree.insert(7)
        self.assertEqual(self.tree.size(), 7)

    def test_contains_false(self):
        self.assertFalse(self.tree.contains(6))

    def test_size(self):
        self.assertEqual(self.tree.size(), 7)
        self.tree.insert(6)
        self.assertEqual(self.tree.size(), 13)

    def test_depth(self):
        self.tree.insert(8)
        self.tree.insert(9)
        self.tree.insert(10)
        self.tree.insert(5)
        self.assertEqual(self.tree.depth(), 4)

    def test_balance_pos(self):
        pass

    def test_balance_neg(self):
        pass

    def test_balance_even(self):
        pass


class EmptyTests(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(None)

    def test_empty_size(self):
        self.assertEqual(self.tree.size(), 0)

    def test_depth_empty(self):
        self.assertEqual(self.tree.depth(), 0)

    def test_empty_balance(self):
        pass


if __name__ == '__main__':
    unittest.main()
