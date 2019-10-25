# 思路：将‘balloon’中出现的字母存入字典中，字母对应键，值表示其在text中出现的次数
# 遍历text中的所有字母，如果有在字典中保存的字母则将该字母出现的次数加一
# 由于‘balloon’中l和o出现了两次，因此在计算最多能组成的字符中，要将字典中对应字母出现的次数除2
# 返回字典中字母出现的最小次数
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i in balloon:
                balloon[i] += 1
        balloon['l'] //= 2
        balloon['o'] //= 2
        camp = 'balon'
        count = len(text)
        for j in camp:
            if balloon[j] < count:
                count = balloon[j]
        return count
