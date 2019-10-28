# 思路：计算连续0的个数即可，但要注意把一些特殊情况考虑进去
# 当花坛只有1个位置或2个位置时，必须这些位置都是0才能种下n<2朵花
# 当花坛位置数大于2时，则计算连续0的个数，由于首部和尾部只需连续两个0就能钟一朵花，而中间位置要3个0，所以初始化连续0个数时将其设为1
# 遍历花坛的位置，如果此位置上的数为1，则将连续0个数置0，如果此位置上的数为0，则将连续0个数加1
# 判断连续0个数是否等于3，如果有3个连续0的话，则将种花数加1，而由于再中间的0位置上种了花，所以此时连续0个数需要减2
# 当遍历到花坛最后一个位置上时，如果此时连续0个数为2，说明最后有两个连续0，是可以再种一朵花的，需要将种花数再加1
# 同样，如果首部也出现连续两个0，也是可以种一朵花的，所以将连续0个数初始化为1，当首部出现两个连续0，则连续0个数为3
# 最后比较允许种花数和给定种花数n，大于等于n则返回True
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            return False
        if len(flowerbed) == 2:
            if flowerbed[0] + flowerbed[1] == 0 and n == 1:
                return True
            return False
        zero_count = 1
        flower_count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                zero_count += 1
            if flowerbed[i] == 1:
                zero_count = 0
            if zero_count == 3:
                flower_count += 1
                zero_count -= 2
            if i == len(flowerbed)-1 and zero_count == 2:
                flower_count += 1
        return flower_count >= n
