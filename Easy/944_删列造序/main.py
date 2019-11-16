# 思路：将所有列序号存入列表中，判断相邻两字符串每一列是否都是非降序排列的，如果不是，将这一列的序号从列序号数组中删除
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        col = list(range(len(A[0])))
        for i in range(len(A)-1):
            for j in set(col):
                if A[i][j] > A[i+1][j]:
                    col.remove(j)
        return len(A[0]) - len(col)
