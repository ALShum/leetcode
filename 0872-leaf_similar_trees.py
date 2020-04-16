# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        #l1 = self.getLeavesRecursive(root1)
        #l2 = self.getLeavesRecursive(root2)
        l1 = self.getLeaves(root1)
        l2 = self.getLeaves(root2)
        print(l1)
        print(l2)
        return l1 == l2

    def getLeavesRecursive(self, node):
        ans = []
        def getLeavesInner(node):
            if not node:
                return
            getLeavesInner(node.left)
            getLeavesInner(node.right)
            if not node.left and not node.right:
                ans.append(node.val)
        getLeavesInner(node)
        return ans

    def getLeaves(self, node):
        ans = []
        q = [node]
        while q:
            n = q.pop()
            if not n.left and not n.right:
                ans.append(n.val)

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return ans
