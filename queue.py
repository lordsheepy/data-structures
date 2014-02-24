
class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        q = QueueObject(value)
        if not self.head:
            self.head = q
        elif not self.tail:
            self.tail = q
            self.head.next = q
        else:
            self.tail.next = q
            self.tail = q
        self.length += 1
        return

    def dequeue(self):
        if self.head:
            response, self.head = self.head.value, self.head.next
            self.length -= 1
            return response
        else:
            raise IndexError

    def length(self):
        return self.length


class QueueObject(object):

    def __init__(self, value):
        self.value = value
        self.next = None
