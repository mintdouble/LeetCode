# 思路：将answer中每个元素及对应出现次数存入字典中，让后比较每个数字及其出现的次数，判断某数字出现的次数与（该数字+1）的关系
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        for i in answers:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        number = 0
        for i in dic.keys():
            if dic[i] <= i+1:
                number += (i+1)
            else:
                if dic[i] % (i+1) == 0:
                    number += ((i+1)*(dic[i]//(i+1)))
                else:
                    number += ((i+1)*((dic[i]//(i+1))+1))
        return number
