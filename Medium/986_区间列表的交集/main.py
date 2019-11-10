# 思路：找到两个区间的所有可能形式，然后根据不同的形式来取交集
# 六种形式： 
# 1          AAAAAA
#                    BBBBB
# 2          AAAAAA
#               BBBBBB
# 3          AAAAAA
#         BBBBBB
# 4          AAAAAA
#    BBBBBB
# 5          AAAAAA
#             BBBB
# 6          AAAAAA
#           BBBBBBBB
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        result = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
                continue
            if A[i][0] < B[j][0] and A[i][1] >= B[j][0] and A[i][1] <= B[j][1]:
                result.append([B[j][0],A[i][1]])
                i += 1
                continue
            if A[i][0] < B[j][0] and A[i][1] > B[j][1]:
                result.append([B[j][0],B[j][1]])
                j += 1
                continue
            if A[i][0] >= B[j][0] and A[i][0] <= B[j][1] and A[i][1] >= B[j][0] and A[i][1] <= B[j][1]:
                result.append([A[i][0],A[i][1]])
                i += 1
                continue
            if A[i][0] >= B[j][0] and A[i][0] <= B[j][1] and A[i][1] > B[j][1]:
                result.append([A[i][0],B[j][1]])
                j += 1
                continue
            if A[i][0] > B[j][1]:
                j += 1
                continue
        return result
