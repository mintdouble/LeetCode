# 思路：主要分两种情况讨论，当k=0时，需要统计数组中不同数字出现的次数，出现两次及两次以上的的数字就是K-diff数对
# 当 k>0 时，将列表转成集合，去掉重复数字，判断集合中的数字+k是否在集合中，如果在，则也为K-diff数对
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        setnums = set(nums)
        count = 0
        if k == 0:
            dic = {}
            for i in nums:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
            for i in dic.values():
                if i > 1:
                    count += 1
        if k > 0:
            for i in setnums:
                if (i+k) in setnums:
                    count += 1
        return count
