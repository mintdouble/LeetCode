# 思路：将n右移一位再与原异或，如果n中所有相邻位不相同，则结果得到的是全1的数，即2^N-1，N为n的二进制位数
import math
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return (n^(n>>1)) == 2**(int(math.log(n,2))+1)-1
