# 思路：统计出现奇数次的行数和出现奇数次的列数。最后为奇数的单元格为：
# 所有单元格减去奇数次行数与奇数次列数相交的单元格数再减去偶数次行数与偶数次列数相交的部分
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row,col = {},{}
        for i in indices:
            if i[0] in row:
                row[i[0]] += 1
            else:
                row[i[0]] = 1
            if i[1] in col:
                col[i[1]] += 1
            else:
                col[i[1]] = 1
        odd_row,odd_col = 0,0
        for i in row.keys():
            if row[i] % 2 != 0:
                odd_row += 1
        for i in col.keys():
            if col[i] % 2 != 0:
                odd_col += 1
        return n*m - odd_row*odd_col - (n-odd_row)*(m-odd_col)
