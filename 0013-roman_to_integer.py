## Roman numerals are normally decreasing: XVIII
## Exceptions are things like IV or XL
## Inspect characters 2 at a time and look for an increasing sequence
class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        s = list(s)[::-1]

        while s:
            cur_char = s.pop()
            cur_amt = sym.get(cur_char)
            next_amt = sym.get(s[-1] if s else '', 0)
            if cur_amt < next_amt:
                total += next_amt - cur_amt
                s.pop()
            else:
                total += cur_amt
        return total