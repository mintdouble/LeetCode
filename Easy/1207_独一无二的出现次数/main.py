# 思路：建立字典保存arr数组中的元素，值为对应元素出现的次数
# 将字典中所有的值存入一个集合中，因为集合中不允许元素重复，因此如果有元素出现的次数相同的话，则集合的长度会减小
# 如果集合的长度等于字典中所有键组成的列表的长度，则说明没有出现次数相同的元素
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dic = {}
        for i in arr:
            if i in arr_dic:
                arr_dic[i] += 1
            else:
                arr_dic[i] = 1
        arr_set = set(arr_dic.values())
        return len(arr_dic) == len(arr_set)
