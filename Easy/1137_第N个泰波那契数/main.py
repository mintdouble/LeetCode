# 思路：定义一个列表维护前三个泰波那契数Tn,Tn+1,Tn+2即可，每次更新这三个数
class Solution:
    def tribonacci(self, n: int) -> int:
        Tn = [0,1,1]
        i = 0
        while i < n - 2:
            Tn[i%3] = sum(Tn)
            i += 1
        return Tn[n%3]
