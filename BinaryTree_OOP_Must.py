

class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.RightNode = None
        self.LeftNode = None

    def insertRight(self,newnode):


        if self.RightNode == None:
             self.RightNode = BinaryTree(newnode)
        else:

            t = BinaryTree(newnode)
            t.RightNode = self.RightNode
            self.RightNode = t

    def insertLeft(self, newnode):

        if self.LeftNode == None:
            self.LeftNode = BinaryTree(newnode)
        else:

            t = BinaryTree(newnode)
            t.LeftNode = self.LeftNode
            self.LeftNode = t

    def getRightNode(self):
        return self.RightNode

    def getLeftNode(self):
        return self.LeftNode

    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key

r = BinaryTree("a")
print(r.getRootVal())
r.insertLeft(1)
r.insertRight(2)

print(r.getLeftNode().getRootVal())
print(r.getRightNode().getRootVal())

