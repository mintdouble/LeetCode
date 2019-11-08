# 思路：通过对数函数找到i，j的上界，再遍历i,j寻找符合条件的数存入集合中
import math
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        x_max,y_max = 1,1
        if x != 1:
            x_max = int(math.log(bound, x)) + 1
        if y != 1:
            y_max = int(math.log(bound, y)) + 1
        for i in range(x_max):
            for j in range(y_max):
                if x**i + y**j <= bound:
                    result.add(x**i+y**j)
                else:
                    break
        return list(result)
