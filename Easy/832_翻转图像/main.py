# 思路：逆序求1-数组元素即可
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in A:
            result.append([1-i[j] for j in range(len(i)-1,-1,-1)])
        return result
