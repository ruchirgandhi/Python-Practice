# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



'''
102. Binary Tree Level Order Traversal


Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # Base case
        if root is None:
            return []
        results = []
        q = collections.deque([root])

#deque([TreeNode{val: 3, left:
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
            results.append(temp)

        return results

s = Solution()

s.levelOrder([3,9,20,null,null,15,7])