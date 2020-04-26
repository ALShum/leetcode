## This uses a level-order traversal, see also 0116 for a similar problem using recursion

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
        if not root:
            return root
        cur_level = [root]
        next_level = []
        while cur_level:
            dummy = Node(None)
            prev = dummy
            n = cur_level.pop(0)
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)

            if not cur_level:
                for n in next_level:
                    prev.next = n
                    prev = prev.next
                cur_level = next_level[:]
                next_level = []
                dummy.next = None
        return root
