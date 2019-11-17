# 思路：利用双指针，奇指针指向奇数位的数，偶指针指向偶数位上的数，奇指针遇到奇数以及偶指针遇到偶数都向后移动，否则交换两数
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i,j = 0,1
        while i < len(A) - 1 and j < len(A):
            if (A[i]&1) == 0:
                i += 2
            else:
                if (A[j]&1) == 1:
                    j += 2
                else:
                    A[i],A[j] = A[j],A[i]
                    i += 2
                    j += 2
        return A
