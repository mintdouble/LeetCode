# 思路：计算前K个数的和，然后每次从尾部加一个新数，从头部减一个旧数，看和是否变大，不用每次都对K个数求和
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsumk = sum(nums[0:k])
        sumk = sum(nums[0:k])
        i = 0
        while i <= len(nums)-k-1:
            sumk += (nums[i+k] - nums[i])
            if sumk > maxsumk:
                maxsumk = sumk            
            i += 1
        return maxsumk / k
