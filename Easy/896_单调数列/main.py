# 设置了两个指针分别表示递增和递减，如果递增指针和递减指针都没有指向当前元素说明，列表不是递增或递减的
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i,j = 0,0
        for k in range(len(A)-1):
            if A[k] <= A[k+1]:
                i += 1
            if A[k] >= A[k+1]:
                j += 1
            if i != k+1 and j != k+1:
                return False
        return True
