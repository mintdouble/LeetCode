# 思路：当数组长度小于3或者第一个元素就大于第二个元素则一定不是山脉数组
# 只需要判断山脉的右边是否是递减的数组，右边一旦出现后一个数大于前一个数则不是山脉数组
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] > A[1]:
            return False
        flag = False
        i = 0
        while i < len(A) - 1:
            if A[i] == A[i+1]:
                return False
            if flag and A[i] < A[i+1]:
                break
            if A[i] > A[i+1]:
                flag = True
            i += 1
        return flag and i == len(A) - 1
