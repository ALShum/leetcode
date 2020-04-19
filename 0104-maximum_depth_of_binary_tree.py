# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        L = self.maxDepth(root.left)
        R = self.maxDepth(root.right)

        return max(L, R) + 1
