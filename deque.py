

class Deque(object):
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


s = Deque()

s.addFront(1)
s.addRear(10)
s.addFront(2)
s.addRear(9)
print(s.removeRear())
print(s.removeFront())
print(s.size())
print(s.removeRear())
print(s.removeFront())
print(s.size())
print(s.isEmpty())






