


class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class  LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_start(self, data):

        self.numOfNodes = self.numOfNodes +1
        new_node = Node(data)


        if self.head == None:
            self.head = new_node
        else:
            # we need to move existing head node to right and add new node in front
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self,data):

        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def size_of_LinkedList(self):
        return self.numOfNodes

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode


    def remove(self,data):

        if self.head == None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        if actual_node == None:
                return

        self.numOfNodes = self.numOfNodes - 1

        if previous_node == None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode







s = LinkedList()


s.insert_start(1)
s.insert_start(1.5)
s.insert_start("Adam")
s.insert_start("Ruchir")
s.insert_end(2)
s.insert_end(10)

print(s.traverse())
print(s.size_of_LinkedList())
s.remove(1)
s.remove(1.5)
print("------------")
print(s.traverse())
print(s.size_of_LinkedList())





