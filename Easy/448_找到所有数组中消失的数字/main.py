# 思路：用的是集合中的减操作，有些过于依赖内置的函数了
# 应当使用数组中元素，与该元素值相等的下标对应的元素取负数，最后整个数组中仍为正数的元素的下标即为未出现的数字
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1)) - set(nums))
