# 思路：大小写字母的ASCII码相差32，根据ASCII码加32得到小写字母
class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ''
        for i in str:
            if i >= 'A' and i <= 'Z':
                s += chr(ord(i)+32)
            else:
                s += i
        return s
