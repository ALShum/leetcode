## Check if X-positions for sq1 is inside sq2 or if X-positions for sq2 inside sq1
## Similar check is run for Y-positions

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_l, y_l, x_r, y_u = rec1
        x2_l, y2_l, x2_r, y2_u = rec2
        cond1 = self.isXOverlap(x_l, x_r, x2_l, x2_r)
        cond2 = self.isYOverlap(y_l, y_u, y2_l, y2_u)
        return cond1 and cond2

    def isXOverlap(self, x_l, x_r, x2_l, x2_r):
        if x_l < x2_l < x_r:
            return True
        if x_l < x2_r < x_r:
            return True
        if x2_l < x_l < x2_r:
            return True
        if x_l < x2_l < x_r:
            return True
        return False

    def isYOverlap(self, y_l, y_u, y2_l, y2_u):
        if y_l < y2_l < y_u:
            return True
        if y_l < y2_u < y_u:
            return True
        if y2_l < y_l < y2_u:
            return True
        if y2_l < y_u < y2_u:
            return True
        return False

