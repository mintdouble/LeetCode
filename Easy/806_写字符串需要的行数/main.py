# 思路：逐个相加，如果长度大于100，则行计数加一，重新相加
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        count_row,ever_row_sum = 1,0
        for i in S:
            if ever_row_sum + widths[ord(i)-ord('a')] > 100:
                count_row += 1
                ever_row_sum = widths[ord(i)-ord('a')]
            else:
                ever_row_sum += widths[ord(i)-ord('a')]
        return [count_row, ever_row_sum]
