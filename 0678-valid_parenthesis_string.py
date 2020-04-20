## Greedy solution
## keep a minimum possible number of ( and max possible (
## if the max possible is < 0 this means an invalid string:  (**))))
## if lower count is less than zero, reset to 0 as the special character could be used instead

class Solution:
    def checkValidString(self, s: str) -> bool:
        lcount, hcount = 0, 0
        for c in s:
            lcount += 1 if c == '(' else -1
            hcount += 1 if c != ')' else -1
            if hcount < 0:
                break
            lcount = max(lcount, 0)

        return lcount == 0
