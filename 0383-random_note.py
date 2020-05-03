class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        r = {}

        for c in magazine:
            m[c] = m.get(c, 0) + 1
        for c in ransomNote:
            r[c] = r.get(c, 0) + 1
            if r[c] > m.get(c, 0):
                return False
        return True
