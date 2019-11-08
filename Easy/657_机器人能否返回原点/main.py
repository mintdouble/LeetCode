# 思路：判断U和D，L和R的数量是否相等
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count1,count2 = 0,0
        for i in moves:
            if i == 'U':
                count1 += 1
            elif i == 'D':
                count1 -= 1
            elif i == 'L':
                count2 += 1
            else:
                count2 -= 1
        return count1 == 0 and count2 == 0
