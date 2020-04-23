# Technically we use a list which is O(n) for inserting in the front
# Just replace this with a queue implementation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        zig = [root]
        zag = []
        zig_elems = []
        zag_elems = []
        useZig = True
        while zig or zag:
            row = zig_elems if useZig else zag_elems
            q = zag if useZig else zig
            n = zig.pop(0) if useZig else zag.pop(0)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
            row.append(n.val) if zig_elems else row.insert(0, n.val)

            if not zag:
                useZig = True
                if zag_elems:
                    ans.append(zag_elems)
                zag_elems = []
            if not zig:
                useZig = False
                if zig_elems:
                    ans.append(zig_elems)
                zig_elems = []
        return ans
