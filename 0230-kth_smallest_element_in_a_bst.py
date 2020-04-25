## Do an iterative in-order traversal and just keep a count until you visit the k-th element
## See 0094 for recursive and iterative in-order traversal of a tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cur = root
        q = []
        k_count = 1
        while q or cur:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            if k_count == k:
                return cur.val
            k_count += 1
            cur = cur.right
        return None

