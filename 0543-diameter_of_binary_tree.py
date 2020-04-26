# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_so_far = 1
        def maxFromHere(n):
            if not n:
                return 0
            L = maxFromHere(n.left)
            R = maxFromHere(n.right)
            self.max_so_far = max(self.max_so_far, L + R + 1)
            return max(L,R) + 1
        maxFromHere(root)
        return self.max_so_far - 1
