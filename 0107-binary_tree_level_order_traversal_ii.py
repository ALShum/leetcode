## Just do a regular level order traversal and reverse the list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        elem = []
        if not root:
            return elem

        root.level = 0
        def levelOrderInner(root):
            if len(elem) == root.level:
                elem.append([])
            elem[root.level].append(root.val)

            if root.left:
                root.left.level = root.level + 1
                levelOrderInner(root.left)
            if root.right:
                root.right.level = root.level + 1
                levelOrderInner(root.right)
        levelOrderInner(root)
        elem.reverse()
        return elem
