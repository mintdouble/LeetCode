# 思路：从左往右遍历数组，half中保留前i个数据的和，即每次前进一格，将half加上i，判断2倍的half与i+1的和是否等于所有数据的和，如果相等说明i+1是中心索引
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_num = sum(nums)
        half = 0
        for i in range(len(nums)):
            if 2 * half + nums[i] == sum_num:
                return i
            half += nums[i]
        return -1
