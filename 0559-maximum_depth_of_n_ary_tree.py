"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        mx_depth = 0
        for c in root.children:
            mx_depth = max(self.maxDepth(c), mx_depth)

        return mx_depth + 1
