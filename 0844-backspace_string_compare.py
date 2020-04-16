## Iterate backwards and count backspaces
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = self.processBackspace(S)
        T = self.processBackspace(T)
        return S == T

    def processBackspace(self, s):
        bspace_cnt = 0
        ans = ""
        for i in range(0, len(s))[::-1]:
            if s[i] == '#':
                bspace_cnt += 1
            elif bspace_cnt > 0:
                bspace_cnt -= 1
            else:
                ans += s[i]
        return ans[::-1]
