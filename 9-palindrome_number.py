class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        #return x_str == x_str[::-1]

        for i in range(0, len(x_str)):
            if x_str[i] != x_str[len(x_str) - i - 1]:
                return False
        return True