class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        if len(self.s) == 0:
            mn = float('inf')
        else:
            mn = self.getMin()
        mn = min(mn, x)
        self.s.append((x, mn))

    def pop(self) -> None:
        if len(self.s) > 0:
            self.s.pop()

    def top(self) -> int:
        if len(self.s) == 0:
            return None
        elem, _ = self.s[-1]
        return elem

    def getMin(self) -> int:
        if len(self.s) == 0:
            return None
        _, mn = self.s[-1]
        return mn

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()