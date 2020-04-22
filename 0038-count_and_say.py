class Solution:
    def countAndSay(self, n: int) -> str:
        d = 1
        if n == 1:
            return str(d)
        for i in range(1, n):
            d = self.runLengthEncode(d)
        return str(d)

    def runLengthEncode(self, n):
        n = str(n)

        prev = n[0]
        count = 0
        result = ""
        for c in n:
            if c == prev:
                count += 1
            else:
                result += str(count) + str(prev)
                prev = c
                count = 1
        if count:
            result += str(count) + str(prev)
        return result
