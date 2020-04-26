## just store the ones you've seen before
class Solution:
    def isHappy(self, n: int) -> bool:
        seenBefore = set()
        while n not in seenBefore:
            seenBefore.add(n)
            new_n = 0

            s = str(n)
            for c in s:
                new_n += int(c) ** 2
            n = new_n
            if n == 1:
                return True
        return False
