# 思路：返回x坐标的最小值与y坐标最小值的乘积，因为坐标值越小加1的次数越多，所以最大值集中在矩阵的左上角
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return m*n if len(ops) < 1 else min([x[0] for x in ops]) * min(x[1] for x in ops)
