


class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def nthNode(n, head):

        left_pointer = head
        right_pointer = head

        for i in range(n-1):

            ### edge case####
            if not right_pointer.nextnode:
                return LookupError("Error N is larger than linked list")
            ####

            right_pointer = right_pointer.nextnode

        while right_pointer.nextnode:

            right_pointer = right_pointer.nextnode
            left_pointer = left_pointer.nextnode


            return left_pointer

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e



target = Node.nthNode(1,b)

print(target.value)


