


def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):

    t = root.pop(1)

    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [],[]])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(1)

print(insertLeft(r,2))
print(insertRight(r,3))

print(setRootVal(r,10))
print(r)

print(getLeftChild(r))
print(getRightChild(r))