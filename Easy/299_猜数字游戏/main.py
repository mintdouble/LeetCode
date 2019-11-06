# 思路：先统计奶牛的个数，再统计公牛的个数，奶牛的统计次数包含了公牛的次数，差值就是实际奶牛的个数。
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {}
        for i in range(len(secret)):
            if secret[i] in dic:
                dic[secret[i]][0] += 1
                dic[secret[i]].append(i)
            else:
                dic[secret[i]] = [1,i]
        countA,countB = 0,0
        for j in range(len(guess)):
            if guess[j] in dic:
                if dic[guess[j]][0]> 0:
                    countB += 1
                    dic[guess[j]][0] -= 1
                if j in dic[guess[j]][1:]:
                    countA += 1
        return str(countA) + 'A' + str(countB-countA) + 'B'
