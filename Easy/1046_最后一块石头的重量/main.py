# 思路：对石头排序，每次取后面的两块进行相减，差值插入到原列表中，相减的两个石头从列表中剔除，对列表重新排序，重复操作
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        length = len(stones)
        for i in range(length-1):
            stones.insert(0,stones[-1] - stones[-2])
            stones.pop()
            stones.pop()
            stones.sort()
        return stones[-1]
            
