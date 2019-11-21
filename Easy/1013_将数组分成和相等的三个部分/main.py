# 思路：首尾遍历，判断首尾是否分别等于总和的1/3，如果找到则返回True，否则False
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        else:
            left,right = 0,0
            i,j = 0,len(A)-1
            A_1_3 = sum(A)//3
            while i < j:
                if left != A_1_3:
                    left += A[i]
                    i += 1
                if  right != A_1_3:
                    right += A[j]
                    j -= 1
                if left == A_1_3 and right == A_1_3:
                    return True
            return False
