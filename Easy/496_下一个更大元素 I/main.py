# 思路：nums2的元素和下标存入字典，找到nums1中的元素在nums2中的位置，从该位置往后查找比其大的第一个数
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums2)):
            dic[nums2[i]] = i 
        for i in range(len(nums1)):
            j = dic[nums1[i]]+1
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    nums1[i] = nums2[j]
                    break
                j += 1
            if j == len(nums2):
                nums1[i] = -1
        return nums1
