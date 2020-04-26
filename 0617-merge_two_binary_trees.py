# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def mergeInner(n1, n2):
            if not n1:
                return n2
            if not n2:
                return n1
            n1.val += n2.val
            n1.left = mergeInner(n1.left, n2.left)
            n1.right = mergeInner(n1.right, n2.right)
            return n1
        return mergeInner(t1, t2)

    ## The iterative method looks ahead at each node's left/right children
    def mergeTrees(self, t1,t2):
        if not t1:
            return t2
        q = [(t1,t2)]
        while q:
            n1,n2 = q.pop()
            if not n1 or not n2:
                continue
            n1.val += n2.val
            if not n1.left:
                n1.left = n2.left
            else:
                q.append((n1.left, n2.left))

            if not n1.right:
                n1.right = n2.right
            else:
                q.append((n1.right, n2.right))
        return t1