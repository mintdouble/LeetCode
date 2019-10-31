# 思路：由于Python带有转二进制和转十进制的函数，这里就投机取巧直接用了，可以通过移位运算，将低位的数移到高位上来
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = bin(n)
        bin_n ='0' * (34-len(bin_n)) + bin_n[2:] + 'b0'
        return int(bin_n[::-1], 2)
