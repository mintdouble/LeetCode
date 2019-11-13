# 思路：对撞指针，遇到I就把正序的指针索引存入，遇到D就把逆序的指针索引存入
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i,j = 0,len(S)
        result = []
        for k in S:
            if k == 'I':
                result.append(i)
                i += 1
            else:
                result.append(j)
                j -= 1
        result.append(i)
        return result
