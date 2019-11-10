class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        summary = 0
        for i in self.dic.keys():
            if len(i) >= len(prefix) and i[:len(prefix)] == prefix:
                summary += self.dic[i]
        return summary


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
