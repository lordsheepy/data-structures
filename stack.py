class Stack(object):

    def __init__(self):
        self.head = None

    def push(self, value):
        next, self.head = self.head, Node(value)
        self.head.next = next

    def pop(self):
        if self.head:
            value, self.head = self.head.value, self.head.next
            return value
        else:
            raise IndexError


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value
