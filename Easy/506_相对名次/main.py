# 思路：对成绩数组进行排序，排名刚好与顺序相反
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_sort = sorted(nums)
        dic = {}
        for i in range(len(nums)):
            dic[nums_sort[i]] = str(len(nums)-i)
        if len(nums) > 0:
            dic[nums_sort[-1]] = 'Gold Medal'
        if len(nums) > 1:
            dic[nums_sort[-2]] = 'Silver Medal'
        if len(nums) > 2:
            dic[nums_sort[-3]] = 'Bronze Medal'
        score = []
        for i in nums:
            score.append(dic[i])
        return score
