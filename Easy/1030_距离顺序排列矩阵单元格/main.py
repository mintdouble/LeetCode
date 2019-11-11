# 思路：把所有点到（r0,c0）的距离都求出来，按照距离的大小顺序进行排序
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dic = {}
        result = []
        for i in range(R):
            for j in range(C):
                distance = abs(i-r0) + abs(j-c0)
                if distance in dic:
                    dic[distance].append([i,j])
                else:
                    dic[distance] = [[i,j]]
        for i in sorted(dic.keys()):
            result.extend(dic[i])
        return result
