class BinaryTree(object):

    def __init__(self, value=None):
        # try:
        #     int(value)
        # except TypeError:
        #     raise
        self.value = value
        self.greater = None
        self.lesser = None

    def insert(self, value):
        """Insert an integer into a binary tree"""
        if value == self.value:
            return
        elif value > self.value:
            if self.greater is None:
                self.greater = BinaryTree(value)
                return
            self.greater.insert(value)
        elif value < self.value:
            if self.lesser is None:
                self.lesser = BinaryTree(value)
                return
            self.lesser.insert(value)

    def contains(self, value):
        """Determine whether value is contained in binary tree"""
        try:
            if value == self.value:
                return True
            elif value > self.value:
                return self.greater.contains(value)
            elif value < self.value:
                return self.lesser.contains(value)
        except AttributeError:
            return False

    def size(self, total=0):
        """Returns total of all values within binary tree"""
        try:
            total += self.value
        except TypeError:
            return 0

        if self.lesser:
            total += self.lesser.size()
        if self.greater:
            total += self.lesser.size()
        return total

    def depth(self):
        if not self.value:
            return 0
        try:
            a = self.greater.depth()
        except:
            a = 0
        try:
            b = self.lesser.depth()
        except:
            b = 0
        return max(a, b) + 1

    def balance(self):
        try:
            a = self.greater.depth()
        except:
            a = 0
        try:
            b = self.lesser.depth()
        except:
            b = 0
        return a - b
