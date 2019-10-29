# 思路：将5元和10元存入零钱字典中，如果收到的是5元，则存入字典中，如果是10元，则先查找字典中是否有5元零钱找零
# 如果没有，则返回False，如果有，则将字典中5元零钱拿出一张，将10元零钱存入字典中
# 如果收到的是20元，则同样判断字典中是否有5元零钱，如果没有则返回False，如果有，则判断5元零钱是否小于3张和是否有10元零钱，如果同时满足，则返回False
# 如果有没有同时满足所有条件，则可以找零20元，接下来判断是否有10元零钱，如果有则从字典中取出一张10元零钱和一张5元零钱，如果没有，则从字典中取出3张5元
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {'5':0, '10':0}
        for i in bills:
            if i == 5:
                change['5'] += 1
            if i == 10:
                if change['5'] < 1:
                    return False
                else:
                    change['5'] -= 1
                    change['10'] += 1
            if i == 20:
                if change['5'] < 1:
                    return False
                else:
                    if change['5'] < 3 and change['10'] < 1:
                        return False
                    else:
                        if change['10'] > 0:
                            change['10'] -= 1
                            change['5'] -= 1
                        else:
                            change['5'] -= 3
        return True
