# 思路：在方格的周围加一圈0的边，然后遍历方格中的点，如果为1，则判断其上下左右为0的个数就是该点的临海面，周长就是所有点的临海面之和
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        perimeter = 0
        if h > 0:
            for i in grid:
                i.insert(0,0)
                i.append(0)
            grid.insert(0,[0]*(w+2))
            grid.append([0]*(w+2))
            for i in range(1,h+1):
                for j in range(1,w+1):
                    if grid[i][j] == 1:
                        perimeter += (4-(grid[i-1][j]+grid[i][j+1]+grid[i+1][j]+grid[i][j-1]))
        return perimeter
