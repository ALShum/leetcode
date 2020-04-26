## Use 4 and 5 as an example:
## 4: if p1 chooses 1,2,3 then p2 chooses 3,2,1
## 5: if p1 choose 2,3 then p1 chooses 3,2 but if p1 choose 1, p2 cannot win as the case reduces to the example with 4
## Strategy: p1 just has to avoid multiples of 4
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
