# 思路：其他元素都只出现一次，那么只需要判断出现过两次的元素就是重复N次的元素，也就只需要判断前N+2个元素即可
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = {}
        for i in range((len(A)//2)+2):
            if A[i] in dic:
                return A[i]
            else:
                dic[A[i]] = A[i]
