## Two pointer solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxArea = 0
        while i < j:
            print((i,j))
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            maxArea = max(maxArea, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea