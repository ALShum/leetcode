# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def levelOrderInner(root, level = 0):
            if not root:
                return
            if len(ans) == level:
                ans.append([])
            ans[level].append(root.val)
            levelOrderInner(root.left, level + 1)
            levelOrderInner(root.right, level + 1)
        levelOrderInner(root, level = 0)
        return ans

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        root.level = 0
        q = [root]
        while q:
            node = q.pop(0)
            if len(ans) == node.level:
                ans.append([])
            ans[node.level].append(node.val)
            if node.left:
                node.left.level = node.level + 1
                q.append(node.left)
            if node.right:
                node.right.level = node.level + 1
                q.append(node.right)
        return ans