# 思路：将对应数字和其出现频次保存到字典中，遍历不重复的所有数字，如果该数字+1也在字典中，则计算该数字频次和该数字+1的频次是否是最大值
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        setnums = set(nums)
        maxlen = 0
        for i in setnums:
            if i+1 in setnums:
                if maxlen < dic[i] + dic[i+1]:
                    maxlen = dic[i] + dic[i+1]
        return maxlen
