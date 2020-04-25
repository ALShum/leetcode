class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        m = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
        ans = []
        def backtrack(digits, cur_str, max_len):
            if len(cur_str) == max_len:
                ans.append(cur_str)
                return
            if len(digits) == 0:
                return
            possible = m.get(digits[0])
            for p in possible:
                backtrack(digits[1:], cur_str + p, max_len)
        backtrack(digits, "", len(digits))
        return ans