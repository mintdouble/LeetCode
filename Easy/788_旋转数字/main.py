# 思路：只要数字中出现了3，4，7则一律不是好数；否则，如果2，5，6，9出现在数字中则是好数
class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(N+1):
            flag = False
            for j in set(str(i)):
                if j in ['3','4','7']:
                    flag = False
                    break
                elif j in ['2','5','6','9']:
                    flag = True
                else:
                    continue
            if flag:
                count += 1
        return count
