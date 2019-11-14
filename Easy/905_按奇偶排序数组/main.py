# 思路：把奇数和偶数分别选出来，然后组合
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        dic = {0:[],1:[]}
        for i in A:
            dic[(i&1)].append(i)
        return dic[0] + dic[1]
