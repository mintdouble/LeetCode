# 思路：根据以数组元素为下标的元素取负，最后不是负数的元素的下标就是缺失的数字
# 需要注意的是，如果有正数，那么返回正数的索引，如果没有，则返回0的索引
# 其他方法：用0-n的等差数列求和减去数组中所有元素求和的差值；或者采用异或的方法令数组中的元素与0-n进行异或消除重复元素，剩余的元素就是缺失的数字
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(1)
        for i in nums[0:len(nums)-1]:
            nums[abs(i)] = -nums[abs(i)]
        index = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
            if nums[i] == 0:
                index = i
        return index
