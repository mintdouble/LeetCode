# 思路：先将数字转化成二进制形式，再交换其中的0和1的位置，再转化成十进制
class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        bin_num = bin_num.replace('0','2')
        bin_num = bin_num.replace('1','0')
        bin_num = bin_num.replace('2','1')
        return int(bin_num, 2)
