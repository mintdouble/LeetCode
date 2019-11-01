# 思路：多观察几组数据就能发现规律，各位相加的结果就是就是该数对9取余数，如果余数为0，则结果为9，不为0则结果为余数，0本身除外
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return num%9 if num%9 != 0 else 9
