import unittest
from data_structures.binarytree import BinaryTree as Tree


class BinaryTreeTests(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(7)

    def test_insert(self):
        self.tree.insert(9)
        self.assertTrue(self.tree.contains(9))

    def test_reinsert(self):
        self.tree.insert(7)
        self.assertEqual(self.tree.size(), 1)

    def test_contains_false(self):
        self.assertFalse(self.tree.contains(6))

    def test_size(self):
        self.assertEqual(self.tree.size(), 1)
        self.tree.insert(6)
        self.assertEqual(self.tree.size(), 2)

    def test_depth(self):
        self.tree.insert(8)
        self.tree.insert(9)
        self.tree.insert(10)
        self.tree.insert(5)
        self.assertEqual(self.tree.depth(), 4)

    def test_balance_pos(self):
        self.tree.insert(10)
        self.tree.insert(8)
        self.tree.insert(9)
        self.assertEqual(self.tree.balance(), 3)

    def test_balance_neg(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(9)
        self.assertEqual(self.tree.balance(), -1)

    def test_balance_even(self):
        self.tree.insert(10)
        self.tree.insert(4)
        self.assertEqual(self.tree.balance(), 0)


class EmptyTests(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(None)

    def test_empty_size(self):
        self.assertEqual(self.tree.size(), 0)

    def test_depth_empty(self):
        self.assertEqual(self.tree.depth(), 0)

    def test_empty_balance(self):
        self.assertEqual(self.tree.balance(), 0)


class TraversalTests(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(10)
        for i in [5, 15, 4, 6, 14, 16]:
            self.tree.insert(i)

    def test_in_order(self):
        outp = []
        for i in self.tree.in_order():
            outp.append(i)
        self.assertEqual(outp, [4, 5, 6, 10, 14, 15, 16])

    def test_post_order(self):
        outp = []
        for i in self.tree.post_order():
            outp.append(i)
        self.assertEqual(outp, [4, 6, 5, 14, 16, 15, 10])

    def test_pre_order(self):
        outp = []
        for i in self.tree.pre_order():
            outp.append(i)
        self.assertEqual(outp, [10, 5, 4, 6, 15, 14, 16])

    def test_breadth_first(self):
        outp = []
        for i in self.tree.breadth_first():
            outp.append(i)
        self.assertEqual(outp, [10, 5, 15, 4, 6, 14, 16])


class DeleteTests(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(10)
        for i in [5, 15, 4, 6, 14, 17]:
            self.tree.insert(i)

    def test_delete_two_child(self):
        self.assertTrue(self.tree.contains(5))
        self.tree.delete(5)
        self.assertFalse(self.tree.contains(5))
        self.assertTrue(self.tree.contains(4))

    def test_delete_single_child(self):
        self.tree.insert(3)
        self.assertTrue(self.tree.contains(4))
        self.tree.delete(4)
        self.assertFalse(self.tree.contains(4))
        self.assertTrue(self.tree.contains(3))

    def test_delete_no_child(self):
        self.assertTrue(self.tree.contains(4))
        self.tree.delete(4)
        self.assertFalse(self.tree.contains(4))


if __name__ == '__main__':
    unittest.main()
