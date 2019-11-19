# 思路：先对数组排序，然后找相邻两元素的最小绝对值差，遍历数组找到最小值，把等于最小绝对值差的两元素保存下来
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        result = []
        minmum = abs(arr[-1]-arr[0])
        for i in range(len(arr)-1):
            if minmum > abs(arr[i]-arr[i+1]):
                result = []
                result.append([arr[i],arr[i+1]])
                minmum = abs(arr[i]-arr[i+1])
            elif minmum == abs(arr[i]-arr[i+1]):
                result.append([arr[i],arr[i+1]])
            else:
                continue
        return result
