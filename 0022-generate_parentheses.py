## Use backtracking and keep track of number of '('

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []
        def backTrack(cur, cur_bal, n_left_rem):
            if len(cur) == 2 * n:
                solutions.append(cur)

            if n_left_rem > 0:
                backTrack(cur + '(', cur_bal + 1, n_left_rem - 1)
            if cur_bal > 0:
                backTrack(cur + ')', cur_bal - 1, n_left_rem)
        backTrack('(', 1, n - 1)
        return solutions
