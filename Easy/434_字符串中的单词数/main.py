# 思路：按照空格切分字符串，统计切分后的字符列表长度
class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split(' ')
        while '' in s:
            s.remove('')
        return len(s)
