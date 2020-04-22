## Strip out non-alphanumeric, lowercase all strings
## reverse a string and check

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == self.reverse(s)

    def reverse(self, s):
        l, r = 0, len(s)
        s = list(s)
        while l < r:
            s[l], s[r-1] = s[r-1], s[l]
            l+=1
            r-=1
        return ''.join(s)
