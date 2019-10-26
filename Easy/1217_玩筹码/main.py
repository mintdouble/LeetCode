# 思路：筹码移动奇数位的代价为1，移动偶数位的代价为0，因此只需要判断奇数位上的筹码与偶数位上的筹码谁多谁少
# 少的那堆筹码就是所需要求的总代价
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even_number = 0
        for i in chips:
            if i % 2 == 0:
                even_number += 1
        return even_number if even_number <= len(chips) - even_number else len(chips) - even_number
