# 思路：从后往前遍历字符串的字母，如果字符串空则返回0
# 找到第一个不为空格的字母，开始计数。直到遇到空格，则计数结束，如果直到字符串首字母也不为空格的话，同样结束计数，返回计数结果
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        point = len(s) - 1
        start = True
        end = True
        count = 0
        if s == '':
            return 0
        while point >= 0 and (start or end):
            if s[point] != ' ':
                start = False
                count += 1
                point -= 1
                continue
            if start == False and s[point] == ' ':
                end = False
            point -= 1
        return count
