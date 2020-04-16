## Use recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  ## BFS solution
    def hasPathSum(self, root: TreeNode, sum: int, cur = 0) -> bool:
        if not root:
            return False

        if not root.left and not root.right and cur + root.val == sum:
            return True

        return self.hasPathSum(root.left, sum, cur+root.val) or self.hasPathSum(root.right, sum, cur+root.val)


class Solution2:  ## DFS solution
    def hasPathSum(self, root: TreeNode, sum: int, cur = 0) -> bool:
        if not root:
            return False

        L = self.hasPathSum(root.left, sum, cur+root.val)
        R = self.hasPathSum(root.right, sum, cur+root.val)

        if not root.left and not root.right and cur + root.val == sum:
            return True

        return L or R