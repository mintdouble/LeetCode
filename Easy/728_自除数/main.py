# 思路：思想比较简单，判断该数是几位数，求得各位的数，然后判断能否整除
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        div = []
        for i in range(left, right+1):
            if i < 10:
                div.append(i)
                continue
            if i < 100:
                if i % 10 != 0 and (i//10)%10 != 0:
                    if i % (i%10) == 0 and i % ((i//10)%10) == 0:
                        div.append(i)
                continue
            if i < 1000:
                if i % 10 != 0 and (i//10)%10 != 0 and (i//100)%10 != 0:
                    if i % (i%10) == 0 and i % ((i//10)%10) == 0 and i % ((i//100)%10) == 0:
                        div.append(i)
                continue
            if i < 10000:
                if i % 10 != 0 and (i//10)%10 != 0 and (i//100)%10 != 0 and (i//1000)%10 != 0:
                    if i % (i%10) == 0 and i % ((i//10)%10) == 0 and i % ((i//100)%10) == 0 and i % ((i//1000)%10) == 0:
                        div.append(i)
                continue
        return div
