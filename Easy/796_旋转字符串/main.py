# 思路：逐个旋转A的字符，比较其中是否有和B相等的情况
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        for i in range(len(A)):
            if A[i:]+A[0:i] == B:
                return True
        return False
