# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        # Base case
        if root is None:
            return []
        results = []
        q = collections.deque([root])

        # deque([TreeNode{val: 3, left:
        # TreeNode{val: 9, left: None, right: None},
        # right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None},
        # right: TreeNode{val: 7, left: None, right: None}}}])

        while len(q) != 0:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            results.append(temp[-1])   ### THIS IS THE KEY

        return results