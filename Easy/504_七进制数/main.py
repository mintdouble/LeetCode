# 思路：根据“除7倒取余”的方法，将每次除完7后得到的余数保存起来，余数列表的逆序就是转化后的七进制数
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        symbol = ''
        if num < 0:
            symbol = '-'
        remainder = []
        num = abs(num)
        while num > 0:
            remainder.insert(0, str(num%7))
            num //= 7
        return symbol + ''.join(remainder)
