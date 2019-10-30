# 思路：将该数的所有正因子保存到集合中，判断集合中所有元素的和是否等于该数本身
# 寻找正因子采用的是遍历法，但没有从头遍历到尾，当遍历索引能被该数整除时，将遍历索引和除后得到的商存入集合中
# 如果不能被整除，则该遍历索引不是正因子，同时将遍历的上界缩减为该数除以该遍历索引得到的取整数
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        div = set([1])
        i,end = 2,num
        while i < end:
            if num % i == 0:
                div.add(i)
                div.add(num//i)
                i += 1
            else:
                end = num // i
                i += 1
        return sum(div) == num and num != 1
