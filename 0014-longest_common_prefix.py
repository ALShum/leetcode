## Iterate letter by letter for each word and check
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        ans = ""
        min_l = min(len(s) for s in strs)
        for i in range(0, min_l):
            new_l = strs[0][i]
            match = True
            for s in strs:
                if s[i] != new_l:
                    match = False
                    break
            if match:
                ans += s[i]
            else:
                break
        return ans