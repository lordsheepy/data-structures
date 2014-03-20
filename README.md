[![Build Status](https://travis-ci.org/lordsheepy/data-structures.png?branch=master)](https://travis-ci.org/lordsheepy/data-structures)
data-structures
===============


Singly-linked List
------------------


Stack
-----


Queue
-----


Hash Table
----------


make_month
----------
collaborated with mark charyk

binary_search_tree
------------------
http://stackoverflow.com/questions/19191707/printing-max-depth-in-binary-search-tree
Helped me wrap my head around the depth function. Otherwise, the recursion came
relatively easily. Tests for each function were written, then the function
itself. Will add timing tests later tonight.

insertion_sort
--------------
Sorts a list in place. Unittests against presorted, empty, single, and unsorted
lists. Slow but effective. Credit @markcharyk for his best and worst case tests.

merge_sort
----------
Sorts a list by recursively splitting into lists of length one and pulling those
together incrementally. Code structure comes from Wikipedia's explanation of
merge sort, the ifmain timing tests are courtesy of @markcharyk. Many thanks to
him for doing the hard work of figuring out the worst case scenario.