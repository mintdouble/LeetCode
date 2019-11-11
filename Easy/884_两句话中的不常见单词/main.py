# 思路：将A和B中的单词存入字典，值为单词出现的频次，返回只出现一次的单词
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(' ')
        B = B.split(' ')
        C = {}
        for i in A:
            if i in C:
                C[i] += 1
            else:
                C[i] = 1
        for j in B:
            if j in C:
                C[j] += 1
            else:
                C[j] = 1
        return [k for k in C if C[k] < 2]
