# 思路：利用快慢指针，遍历二进制数，计算两个1之间的间隔
class Solution:
    def binaryGap(self, N: int) -> int:
        binN = bin(N)
        i,j,count = 2,3,0
        while j < len(binN):
            if binN[j] == '0':
                j += 1
            else:
                if count < j - i:
                    count = j - i
                i = j
                j += 1
        return count
