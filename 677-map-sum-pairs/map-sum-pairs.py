class MapSum:

    def __init__(self):
        self.hashmap = {}

    def insert(self, key: str, val: int) -> None:
        self.hashmap[key] = val

    def sum(self, prefix: str) -> int:
        sum = 0
        for i in self.hashmap:
            if prefix == i[:len(prefix):]:
                sum += self.hashmap[i]
        return sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)