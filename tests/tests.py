#! /usr/bin/env python

import unittest
import linked_list


class LinkedListTest(unittest.TestCase):

    def test_insert(self):
        my_linklist = linked_list.LinkList()
        my_linklist.insert("This")
        self.assertEqual(my_linklist.head.value, "This")

    def test_pop(self):
        my_linklist = linked_list.LinkList()
        my_linklist.insert("This")
        my_linklist.insert(6)
        my_linklist.insert(True)
        self.assertEqual(my_linklist.pop(), True)

    def test_size(self):
        a = 3
        my_linklist = linked_list.LinkList()
        my_linklist.insert("This")
        my_linklist.insert(6)
        my_linklist.insert(True)
        self.assertEqual(my_linklist.size(), a)

    def test_search(self):
        my_linklist = linked_list.LinkList()
        my_linklist.insert("This")
        my_linklist.insert(6)
        my_linklist.insert(True)
        self.assertEqual(my_linklist.search("This").value, "This")

    def test_searchfalse(self):
        my_linklist = linked_list.LinkList()
        my_linklist.insert("This")
        my_linklist.insert(6)
        my_linklist.insert(True)
        self.assertEqual(my_linklist.search("Stuff"), None)

    def test_remove(self):
        my_linklist = linked_list.LinkList()
        my_linklist.insert("This")
        my_linklist.insert(6)
        my_linklist.insert(True)
        my_linklist.remove("This")
        self.assertNotIn("This", str(my_linklist))

if __name__ == "__main__":
    unittest.main()
