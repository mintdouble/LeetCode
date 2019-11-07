# 思路：因为只有4个数字，所有可能的组合只有24种，将每种组合都计算出来，然后比较，如果是正确的时间形式，则取其中的最大值，如果所有都不正确，则返回空
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        result = ''
        for i in range(4):
            index = [j for j in range(4) if j != i]
            for j in index:
                index2 = [k for k in index if k != j]
                for k in index2:
                    index3 = [m for m in index2 if m != k]
                    for m in index3:
                        time = str(A[i])+str(A[j])+str(A[k])+str(A[m])
                        if time[0] > '2' or (time[0] == '2' and time[1] > '3') or (
                            time[0] == '2' and time[1] < '4' and time[2] > '5') or (time[0] < '2' and time[2] > '5'):
                            continue
                        else:
                            result = max(result, time)
        return '' if result == '' else result[:2] + ':' + result[2:4]
