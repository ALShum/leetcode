## Use recursion but keep track of the path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def findPath(root, sum, cur_path = [], cur_sum = 0):
            if not root:
                return False

            L = findPath(root.left, sum, cur_path + [root.val], cur_sum + root.val)
            R = findPath(root.right, sum, cur_path + [root.val], cur_sum + root.val)

            if not root.left and not root.right and cur_sum + root.val == sum:
                ans.append(cur_path + [root.val])
        findPath(root, sum, [], 0)
        return ans