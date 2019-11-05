# 思路：统计每个数字连续出现的次数
class Solution:
    def countAndSay(self, n: int) -> str:
        num = '1'
        for i in range(1,n):
            tmp = []
            count = 1
            for j in range(len(num)):
                if j == len(num) - 1:
                    tmp.append(str(count))
                    tmp.append(num[-1])
                    break
                if num[j] == num[j+1]:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(num[j])
                    count = 1              
            num = ''.join(tmp)
        return num
