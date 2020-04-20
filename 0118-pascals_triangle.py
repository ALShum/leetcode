class Solution:
    ## Iterative Solution
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            if i == 1:
                ans.append([1,1])
            if i > 1:
                prev = ans[-1]
                row = [1]
                for j in range(1,len(prev)):
                    row.append(prev[j-1] + prev[j])
                row.append(1)
                ans.append(row)
        return ans
