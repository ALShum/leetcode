## keep track of the lower and upper limit for each side of the tree going down

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTinner(root, low, upper):
            if not root:
                return True
            if not (low < root.val < upper):
                return False
            return isValidBSTinner(root.left, low, root.val) and isValidBSTinner(root.right, root.val, upper)
        return isValidBSTinner(root, float('-inf'), float('inf'))