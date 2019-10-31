# 思路：按照等差数列的求和公式推导出Sn与n之间的关系，然后得到关于求n的表达式
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(2*n+0.25)-0.5)
