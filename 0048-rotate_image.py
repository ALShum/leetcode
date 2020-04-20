## It's tricky to make sure we can handle for even & odd number of rows
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #(r,c) > (c, ncols - r - 1)
        #(0,1) > (1,3) > (3,2) > (2,0) #clockwise
        #(0,1) > (ncols - c - 1, r)
        if not matrix:
            return matrix

        nrows = len(matrix)
        ncols = len(matrix[0])
        ## the nrows+1 here makes sure we can handle matrices with odd & even num of rows
        ## we can't have both nrows+1 and ncols+1 because this will double rotate some elements
        for r in range(0, (nrows+1) // 2):
            for c in range(0, ncols // 2):
                top = matrix[r][c]
                right_r, right_c = c, ncols - r - 1
                right = matrix[right_r][right_c]
                bottom_r, bottom_c = right_c, ncols - right_r - 1
                bottom = matrix[bottom_r][bottom_c]
                left_r, left_c = bottom_c, ncols - bottom_r - 1
                left = matrix[left_r][left_c]

                matrix[right_r][right_c] = top
                matrix[bottom_r][bottom_c] = right
                matrix[left_r][left_c] = bottom
                matrix[r][c] = left