# 思路：简单的将guess列表和answer列表中的对应下标的元素进行对比
# 如果相同则计数器加一，但是时间消耗上不是很理想
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0
        for i in range(3):
            if guess[i] == answer[i]:
                count += 1
        return count
