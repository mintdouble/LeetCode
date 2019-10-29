# 思路：对数组排序，最大乘积出现的情况只有两种，一种是出现在最后三个数上，一种是出现在前两个数与最后一个数上，比较两种情况返回大的那个
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[-1]*nums[-2]*nums[-3] if nums[-1]*nums[-2]*nums[-3] > nums[0]*nums[1]*nums[-1] else nums[0]*nums[1]*nums[-1]
