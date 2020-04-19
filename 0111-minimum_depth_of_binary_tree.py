## Depth first search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        L = float('inf')
        R = float('inf')
        if root.left:
            L = self.minDepth(root.left)
        if root.right:
            R = self.minDepth(root.right)

        return min(L, R) + 1
