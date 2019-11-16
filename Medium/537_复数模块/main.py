# 思路：将字符串中表示a和b的数字分割出来，按照乘法运算再组合各系数
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = a[:len(a)-1].split('+')
        b = b[:len(b)-1].split('+')
        return str(int(a[0])*int(b[0])-int(a[1])*int(b[1]))+'+'+str(int(a[0])*int(b[1])+int(a[1])*int(b[0]))+'i'
