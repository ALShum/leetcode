## Use depth first recursion to find height of each node
## Calculate the difference in depth of node.left and node.right
## If difference is more than 1, isBalanced = False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        isBalanced = True
        def findDepth(root):
            if not root:
                return 0
            left_depth = findDepth(root.left)
            right_depth = findDepth(root.right)

            depth = max(left_depth, right_depth) + 1
            balanced = abs(left_depth - right_depth) <= 1
            if not balanced:
                nonlocal isBalanced
                isBalanced = False
            return depth
        findDepth(root)
        return isBalanced
