# 思路：做的有些复杂了，用字典保存每个元素出现的频率，数组的度就是频率的最大值
# 然后找到出现过最大频率的元素，分别得到以这些元素开头和结尾的连续子数组
# 优化：用字典保存每个元素出现的索引即可，最后就不用到原数组中去查找元素
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sort_count = sorted(dic.values())
        if sort_count[-1] == 1:
            return 1
        max_count = [k for (k,v) in dic.items() if v == sort_count[-1]]
        min_len = len(nums)
        for k in max_count:
            i,j = 0,len(nums)-1
            while i < j:
                if nums[i] != k:
                    i += 1
                    continue
                if nums[j] != k:
                    j -= 1
                    continue
                if nums[i] == k and nums[j] == k:
                    break
            min_len = min(min_len, j-i+1)
        return min_len
