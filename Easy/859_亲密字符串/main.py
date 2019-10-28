# 思路：统计A，B两个字符串中不同字符的个数，只有当个数为0和为2时才有可能是亲密字符串，其他情况都不是
# 当个数为0时，需要判断字符串中是否有重复元素，方法是将字符串保存进set集合中，如果有重复元素则集合的长度小于原字符长度，如果有重复字母，则是亲密字符串
# 当个数为2时，比较这两个不同的位置上的字母交位置后是否相同，相同则为亲密字符串
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2 or len(B) < 2:
            return False
        count = 0
        AB = []
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                AB.append(A[i])
                AB.append(B[i])
            if count > 2:
                return False
        if count == 2 and AB[0] == AB[3] and AB[1] == AB[2]:
            return True
        if count == 0 and len(set(A)) != len(A):
            return True
        return False
