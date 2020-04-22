## Sort - O(nlogn), O(1) memory
## Hashmap - O(n) but also O(n) memory

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t
