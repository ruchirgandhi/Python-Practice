class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self,items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()

print("adding new element in a stack")
s.push(1)
print("adding new element in a stack")
s.push(2)
print("removing element from the stack {}".format(s.pop()))
print("adding new element in a stack")
s.push(3)
print("adding new element in a stack")
s.push("Ruchir")
print("size of the stack is {}".format(s.size()))
print(s.peek())
print("checking is stack is empty {}".format(s.isEmpty()))

print("removing element from the stack {}".format(s.pop()))
print("removing element from the stack {}".format(s.pop()))
print("removing element from the stack {}".format(s.pop()))
print("checking is stack is empty {}".format(s.isEmpty()))