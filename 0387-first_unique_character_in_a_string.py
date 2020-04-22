## Use hashmap
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1

        for i in range(len(s)):
            if m.get(s[i], 0) < 2:
                return i
        return -1