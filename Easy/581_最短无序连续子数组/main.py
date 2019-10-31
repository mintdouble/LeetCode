# 思路：将数组与排序后的数组进行对比，相同下标上的数如果不相同，则该数是需要排序的，因此分别从前和从后开始查找第一个不相同的数
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        head = 0
        tail = len(nums) - 1
        flag = True
        while flag and head < tail:
            if nums[head] == nums_sort[head]:
                head += 1
            if nums[tail] == nums_sort[tail]:
                tail -= 1
            if nums[head] != nums_sort[head] and nums[tail] != nums_sort[tail]:
                flag = False
        return 0 if head == tail else tail - head + 1
