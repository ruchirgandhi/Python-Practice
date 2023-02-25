
# FIFO

class Queue(object):
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)


    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



s = Queue()

s.enqueue(2)
s.enqueue("Two")
print(s.pop())
print(s.size())
print(s.pop())
print(s.isEmpty())

