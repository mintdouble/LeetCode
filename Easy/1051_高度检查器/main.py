# 思路：排序后比较相同位置上的元素是否相同
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        true = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if true[i] != heights[i]:
                count += 1
        return count
