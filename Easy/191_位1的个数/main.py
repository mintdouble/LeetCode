# 思路：根据二进制最低位为0能够被2整除，为1不能被2整除，可以将所有位移到最低位来统计1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n % 2 != 0:
                count += 1
            n >>= 1
        return count
