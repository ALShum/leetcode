## just keep track of how many letters are left and keep iterating through the list of letters
class Solution:
    def sortString(self, s: str) -> str:
        s = sorted(s)
        cnt = len(s)
        m = {}
        for ss in s:
            m[ss] = m.get(ss,0) + 1
        letters = list(m.keys())

        ans = ""
        while cnt > 0:
            for l in letters:
                if m.get(l, 0) > 0:
                    ans += l
                    m[l] = m.get(l, 0) - 1
                    cnt -= 1
            letters = letters[::-1]
        return ans

