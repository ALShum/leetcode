## recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        L_sum = self.rangeSumBST(root.left, L, R)
        R_sum = self.rangeSumBST(root.right, L, R)
        ss = root.val if root.val >= L and root.val <= R else 0
        return  L_sum + R_sum + ss
