# 思路：交换之后两人的糖果总量相同，那么设A交换的是a,B交换的是b，那么应该满足sum_A-a+b=sum_B-b+a,就能得到a,b之间的关系
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        fac = int((sum(A)-sum(B)) / 2)
        set_A = set(A) # 不转化成集合就超出时间限制
        for i in B:
            if (i + fac) in set_A:
                return [i+fac, i]
