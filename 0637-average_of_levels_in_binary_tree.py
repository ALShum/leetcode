# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        levels = {}
        root.level = 0
        def levelOrderInner(root):
            sumx, n = levels.get(root.level, (0, 0))
            sumx += root.val
            n += 1
            levels[root.level] = (sumx, n)

            if root.left:
                root.left.level = root.level + 1
                levelOrderInner(root.left)
            if root.right:
                root.right.level = root.level + 1
                levelOrderInner(root.right)

        levelOrderInner(root)
        ans = [levels[k][0] / levels[k][1] for k in levels]
        return ans
