# 思路是创建一个字典将S中所有的字符和其出现的次数映射成键值对
# 遍历J中出现的字符是否在S中，如果出现则将计数器加上该字符健对应的值
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        S_dic = {}
        num = 0
        for i in range(len(S)):
            if S[i] in S_dic:
                S_dic[S[i]] += 1
            else:
                S_dic[S[i]] = 1
        for j in range(len(J)):
            if J[j] in S_dic:
                num += S_dic[J[j]]
        return num
