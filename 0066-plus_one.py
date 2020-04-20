class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = 1
        for i in range(0, len(digits))[::-1]:
            digit = digits[i] + overflow
            overflow = 0
            if digit > 9:
                overflow += 1
                digit -= 10
            digits[i] = digit
        if overflow:
            digits.insert(0, overflow)
        return digits
