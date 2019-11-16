# 思路：把每一列放入数组的每一行里
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(A[0])):
            result.append([j[i] for j in A])
        return result
