"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(root1, root2):
            if not root1 and not root2:
                return
            if root1:
                root1.next = root2
                helper(root1.left, root1.right)
            if root2:
                helper(root2.left, root2.right)
            if root1 and root2:
                helper(root1.right, root2.left)
        helper(root, None)
        return root
