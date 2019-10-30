# 思路：将两数按位异或，求得到的数的二进制表示中1的个数
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        count = 0
        while num > 0:
            if num % 2 != 0:
                count += 1
            num >>= 1
        return count
