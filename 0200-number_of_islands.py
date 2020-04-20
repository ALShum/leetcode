## When an island is found, iterate through neighbors and mark as visited

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        if nrows == ncols == 1:
            return int(grid[0][0])

        visited = [[False] * ncols for i in range(0, nrows)]
        nislands = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1" and not visited[r][c]:
                    visited[r][c] = True
                    nislands += 1
                    q = self.getNeighbors(r, c, nrows, ncols)
                    while q:
                        n_r, n_c = q.pop()
                        if grid[n_r][n_c] == "1" and not visited[n_r][n_c]:
                            q  += self.getNeighbors(n_r, n_c, nrows, ncols)
                            visited[n_r][n_c] = True
        return nislands

    def getNeighbors(self, r, c, nrows, ncols):
        if nrows == 1:
            if c == 0:
                return [(r, c+1)]
            if c == ncols - 1:
                return [(r, c-1)]
            return [(r, c-1), (r, c+1)]
        if ncols == 1:
            if r == 0:
                return [(r+1, c)]
            if r == nrows - 1:
                return [(r-1, c)]
            return [(r+1, c), (r-1, c)]
        if r == 0 and c == 0:
            return [(r+1, c), (r, c+1)]
        if r == 0 and c == ncols - 1:
            return [(r+1, c), (r, c-1)]
        if r == nrows - 1 and c == 0:
            return [(r-1, c), (r, c+1)]
        if r == nrows - 1 and c == ncols - 1:
            return [(r-1, c), (r, c-1)]
        if r == 0:
            return [(r+1, c), (r, c-1), (r, c+1)]
        if r == nrows - 1:
            return [(r-1, c), (r, c-1), (r, c+1)]
        if c == 0:
            return [(r+1, c), (r-1, c), (r, c+1)]
        if c == ncols - 1:
            return [(r+1, c), (r-1, c), (r, c-1)]
        return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
