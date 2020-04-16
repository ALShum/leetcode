## Use an array-list type of approach with an array that gros with elements inserted
## This exercise is trivial if we use a Set() or Map, so it is avoided

# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.b = [False] * 10

    def add(self, key: int) -> None:
        size = len(self.b)
        if key >= size:
            while key >= size: size *= 2
            new_b = [False] * size
            for i in range(len(self.b)):
                new_b[i] = self.b[i]
            self.b = new_b
        self.b[key] = True


    def remove(self, key: int) -> None:
        if key < len(self.b):
            self.b[key] = False


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key >= len(self.b):
            return False
        return self.b[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)