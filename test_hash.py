import unittest
import hash_table


class GetTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_type(self):
        pass

    def test_get_single(self):
        pass

    def test_get_multiple(self):
        pass

    def test_get_empty(self):
        pass


class SetTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_set_type(self):
        pass

    def test_set_single(self):
        pass

    def test_set_collision(self):
        pass


class HashTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_hash(self):
        pass


class BucketTest(unittest.TestCase):

    def setUp(self):
        self.bucket = hash_table.Bucket('this')

    def test_id(self):
        pass

    def test_contain(self):
        pass

    def test_collision(self):
        pass

    def test_set_key_type(self):
        pass


if __name__ == '__main__':
    unittest.main()
