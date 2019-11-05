# 思路：建立字典保存magazine中的字母和出现次数，当ransomNote中出现的字母在字典中存在时，使该字母出现次数减1，如果出现次数已经为0的话，则直接返回False
# 如果字典中不存在该字母，也返回False
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in magazine:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in ransomNote:
            if i in dic and dic[i] != 0:
                dic[i] -= 1
            else:
                return False
        return True
