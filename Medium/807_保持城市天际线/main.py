# 思路：找到每行每列的最大值，每个单元格中的值取该单元格所在行和所在列中的最大值的最小值
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        height = 0
        col_max = []
        row = len(grid)
        col = len(grid[0])
        for i in range(col):
            col_max.append(max([grid[j][i] for j in range(row)]))
        for i in range(row):
            row_max = max(grid[i])
            for j in range(col):   
                height += (min(row_max,col_max[j])-grid[i][j])
        return height
