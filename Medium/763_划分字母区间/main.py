# 思路：统计每个字符出现的起始位置为终结位置，完全不相交的区间才能分割，相交的各区间，取其中最小值为左界，最大值为右界形成新的区间，
# 所有新区间都不相交，每个新区间就是分割的字符串的位置
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        result = []
        for i in range(len(S)):
            if S[i] in dic:
                dic[S[i]][1] = i+1
            else:
                dic[S[i]] = [i+1,i+1]
        start,end = dic[S[0]][0],dic[S[0]][1]
        for i in sorted(dic.values()):
            if i[0] <= end:
                end = max(end, i[1])
            else:
                result.append(end-start+1)
                start, end =i[0], i[1]
        result.append(end-start+1)
        return result
