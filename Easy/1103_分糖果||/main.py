# 思路：找到每个人每轮获得糖果的通项公式，根据通项公式得到求和公式，就可以根据分发轮数一次性得到该人最终获得的糖果总数
import math
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        max_people = int(math.sqrt(2*candies+0.25)-0.5)
        remain_candies = candies - (max_people*(max_people+1)) // 2
        epoch = max_people // num_people
        extra_epoch = max_people % num_people
        result = [0] * num_people
        for i in range(num_people):
            if i < extra_epoch:
                result[i] = (epoch+1)*(2*(i+1)+num_people*epoch)//2
            else:
                result[i] = epoch*(2*(i+1)+num_people*(epoch-1))//2
        result[extra_epoch] += remain_candies
        return result
