# 思路：将数字保存进字典中，如果有重复的数字，则从字典中删除该数字，最后字典中剩下的就是只出现一次的数字
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                del dic[i]
            else:
                dic[i] = i
        return list(dic.values())
