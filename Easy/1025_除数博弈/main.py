# 思路：偶数必赢，奇数必输
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
