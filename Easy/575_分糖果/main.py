# 思路：两种情况，如果糖果的种类数比糖果的数量的一半要多的话，那么能分到的最大的种类数应为糖果数量的一半
# 如果种类数比糖果总数的一半要少的话，那么能分到的最多的种类数就是所有种类数
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return len(set(candies)) if len(set(candies)) < len(candies)//2 else len(candies)//2
