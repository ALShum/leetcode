## Just do a forward fill, for each position total up cost to neighors, track minimum cost
## Becareful of edge cases where ncol == 1 or nrow == 1

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        if nrows == ncols == 1:
            return grid[0][0]
        if nrows == 1:
            return sum(grid[0])
        if ncols == 1:
            return sum([r[0] for r in grid])

        cost = []
        for n in range(nrows):
            cost.append([float('inf')] * ncols)
        cost[0][0] = grid[0][0]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                self.visit(grid, cost, r, c)
        return cost[-1][-1]


    def visit(self, grid, cost, r, c):
        nrows = len(grid)
        ncols = len(grid[0])

        neighbors = self.getNeighbors(r,c, nrows, ncols)
        print(neighbors)
        for n_r, n_c in neighbors:
            cost[n_r][n_c] = min(cost[n_r][n_c], cost[r][c] + grid[n_r][n_c])

    def getNeighbors(self, r, c, nrows, ncols):
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
