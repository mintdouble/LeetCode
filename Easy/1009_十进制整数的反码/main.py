# 思路：先将数转二进制，然后按位取反，再转十进制
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bin_N = bin(N)[2:]
        bin_N = bin_N.replace('1','2')
        bin_N = bin_N.replace('0','1')
        bin_N = bin_N.replace('2','0')
        return int(bin_N,2)
