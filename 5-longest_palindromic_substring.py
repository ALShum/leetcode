class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSoFar = ''
        for i in range(len(s)):
            A = self.checkPalindromeFromHere(s, i, i)
            B = self.checkPalindromeFromHere(s, i, i+1)

            longer_str = A if len(A) > len(B) else B
            maxSoFar = longer_str if len(longer_str) > len(maxSoFar) else maxSoFar
        return maxSoFar

    def checkPalindromeFromHere(self, s, l_ptr, r_ptr):
        while l_ptr >= 0 and r_ptr < len(s):
            if s[l_ptr] != s[r_ptr]:
                break
            l_ptr -= 1
            r_ptr += 1
        return s[l_ptr+1 : r_ptr]
