    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        ans = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans

    def inorderTraversal(self, root: TreeNode):
        cur = root
        q = []
        ans = []
        while q or cur:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans