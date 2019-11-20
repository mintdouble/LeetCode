# 思路：从原矩阵中中取元素放入新矩阵中，注意取得行数和列数如何用取的个数表示即可
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        else:
            reshape = []
            index = 0
            for i in range(r):
                tmp = []
                for j in range(c):
                    tmp.append(nums[index // len(nums[0])][index % len(nums[0])])
                    index += 1
                reshape.append(tmp)
            return reshape
