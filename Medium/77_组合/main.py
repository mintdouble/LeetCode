# 思路：n个数中选k个数的排列组合，这里用二进制数来进行筛选
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        down = int('1'*k,2)
        up = int('1'*k+'0'*(n-k),2)
        result = []
        for i in range(up,down-1,-1):
            bin_i = bin(i)[2:]
            if len(bin_i.replace('0','')) != k:
                continue
            else:
                result.append([n-len(bin_i)+j+1 for j in range(len(bin_i)) if bin_i[j]=='1'])
        return result
