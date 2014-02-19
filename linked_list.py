
class LinkList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        response = "("
        i = self.head
        while i:
            response += str(i.value)
            if not i.nextnode:
                response += ")"
                break
            i = i.nextnode
            response += ", "
        return response

    def insert(self, value):
        nextn = self.head
        self.head = Node(value)
        self.head.nextnode = nextn
        self.length += 1
        return

    def pop(self):
        v = self.head.value
        self.head = self.head.nextnode
        self.length -= 1
        return v

    def size(self):
        return self.length

    def search(self, val):
        current = self.head
        for i in range(self.length):
            if current.value == val:
                return current
            else:
                current = current.nextnode
        return None

    def remove(self, val):
        current = self.head
        previous = None
        for i in range(self.length):
            if current.value == val:
                break
            else:
                previous = current
                current = current.nextnode
        if previous is None and self.head.value == val:
            self.pop()
            return
        previous.nextnode = current.nextnode
        return


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.nextnode = None

    def __str__(self):
        return str(self.value)
