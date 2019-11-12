# 思路：将拿到的钥匙存入集合，从集合中拿出一把钥匙，如果对应的门是开着的，则把钥匙删除；如果是关着的，则把门打开，把房间的钥匙存入集合
# 直到集合中已经没有钥匙后，判断此时门是否全开了
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = dict.fromkeys(range(len(rooms)), False)
        opened[0] = True
        keys = set(rooms[0])
        while len(keys) > 0:
            key = keys.pop()
            if not opened[key]:
                keys.update(rooms[key])
                opened[key] = True
        return not (False in opened.values())
