# 思路：按层旋转，先旋转最外层，然后旋转内层，每次旋转四个元素，从四个角元素开始，直到该层转完
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        head_i, head_j = 0, 0
        tail_i, tail_j = len(matrix) - 1, len(matrix[0]) - 1
        while head_i < tail_i:
            for (i, j) in zip(range(tail_i-head_i), range(tail_j-head_j)):
                tmp = matrix[head_i][head_j+j]
                matrix[head_i][head_j+j] = matrix[tail_i-i][head_j]
                matrix[tail_i-i][head_j] = matrix[tail_i][tail_j-j]
                matrix[tail_i][tail_j-j] = matrix[head_i+i][tail_j]
                matrix[head_i+i][tail_j] = tmp
            head_i += 1
            head_j += 1
            tail_i -= 1
            tail_j -= 1
