## Essentially using an OrderedDict, in py3.7+ regular dictionaries are ordered
## When getting an element, pop it out of the dict and put it back in (to renew item)
## When putting in an item, check if item is in map, if it is, renew item with new value
##      if not, pop out oldest item and replace with new item

#from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}

    def get(self, key: int) -> int:
        elem = self.m.get(key, -1)
        if elem > 0:
            del self.m[key]
            self.m[key] = elem
        return elem

    def put(self, key: int, value: int) -> None:
        k = self.m.keys()
        if key in self.m:
            del self.m[key]
        elif len(k) == self.capacity:
            oldest = next(iter(k))
            del self.m[oldest]
        self.m[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)