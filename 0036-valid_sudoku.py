class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            dup = self.checkDuplicates(self.getRow(board, r))
            if dup:
                return False
        for c in range(len(board[0])):
            dup = self.checkDuplicates(self.getCol(board, c))
            if dup:
                return False
        for r in range(0, 3):
            for c in range(0, 3):
                dup = self.checkDuplicates(self.getCell(board, r, c))
                if dup:
                    return False
        return True

    def getRow(self, board, r):
        return board[r]

    def getCol(self, board, c):
        return [r[c] for r in board]

    def getCell(self, board, r, c):
        rr = range(r * 3, r * 3 + 3)
        cc = range(c * 3, c * 3 + 3)
        return [board[r][c] for r in rr for c in cc]

    def checkDuplicates(self, l):
        s = set()
        for ll in l:
            if ll != '.' and ll in s:
                return True
            s.add(ll)
        return False
