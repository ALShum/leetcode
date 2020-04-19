# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetricInner(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False

            eq = n1.val == n2.val
            c1 = isSymmetricInner(n1.right, n2.left)
            c2 = isSymmetricInner(n1.left, n2.right)
            return eq and c1 and c2
        return isSymmetricInner(root, root)
