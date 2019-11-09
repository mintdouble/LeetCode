# 思路：每次找到最大的元素，然后将其翻转到第一个位置上，再将其翻转到最后的位置上
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        dic = {A[i]:i+1 for i in range(len(A))}
        result = []
        for i in range(len(A),1,-1):
            if dic[i] == i:
                continue
            elif dic[i] == 1:
                result.append(i)
            else:
                result.extend([dic[i],i])
            for j in dic.keys():
                if dic[j] < dic[i]:
                    dic[j] += (i-dic[i])
                elif dic[j] == dic[i]:
                    continue
                else:
                    dic[j] = i + 1 - dic[j]
            del dic[i]
        return result
