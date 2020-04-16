# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        node = None
        def searchBSTinner(root):
            if not root:
                return
            if root.val == val:
                nonlocal node
                node = root
                return
            if val < root.val and root.left:
                searchBSTinner(root.left)
            if root.val < val and root.right:
                searchBSTinner(root.right)
        searchBSTinner(root)
        return node
