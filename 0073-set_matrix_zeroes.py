## we can go through matrix and mark things to be set to zero with a 2
## alternatively we can mark the first row/col with zeros,
## but we must handle the first row/col differently

class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    self.setRow(matrix, r, 2)
                    self.setCol(matrix, r, 2)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 2:
                    matrix[r][c] == 0

    def setRow(self, matrix, r, elem):
        ncols = len(matrix[r])
        matrix[r] = [elem] * ncols

    def setCol(self, matrix, c, elem):
        nrows = len(matrix)
        for r in matrix:
            r[c] = elem

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_col = False
        first_row = False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 and matrix[r][c] == 0:
                    first_row = True
                if c == 0 and matrix[r][c] == 0:
                    first_col = True
                if matrix[r][c] == 0 and r > 0 and c > 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                self.setRow(matrix, r, 0)
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                self.setCol(matrix, c, 0)
        if first_col:
            self.setCol(matrix, 0, 0)
        if first_row:
            self.setRow(matrix, 0, 0)
        print(first_col,first_row)
