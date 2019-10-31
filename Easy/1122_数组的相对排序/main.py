# 思路：将arr1中的元素和对应出现次数存入字典中，遍历arr2中的元素，从字典中查找对应元素，将其存入列表，然后从字典中删除该元素
# 最后对剩下的字典中的元素进行排序后存入列表
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        arr = []
        for i in arr1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in arr2:
            arr.extend([i]*dic[i])
            del dic[i]
        for i in sorted(dic.keys()):
            arr.extend([i]*dic[i])
        return arr
