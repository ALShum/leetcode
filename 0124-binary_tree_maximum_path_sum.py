## At each node, check the maximum sum of L + R + curr, L + this, R + curr, and just curr node
## In the recursion return, return max(L,R) + curr
## and also just curr node (in this case we return from this node up)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSoFar = float('-inf')
        def pathSum(node):
            if not node:
                return 0
            lsum = pathSum(node.left)
            rsum = pathSum(node.right)
            nonlocal maxSoFar
            maxSoFar = max(maxSoFar, lsum + rsum + node.val, lsum + node.val, rsum + node.val, node.val)
            return max(max(lsum, rsum) + node.val, node.val)
        pathSum(root)
        return maxSoFar