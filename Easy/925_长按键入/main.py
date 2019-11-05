# 思路：利用双指针，分别比较name和typed中的字符，如果name中某字符连续出现次数多余typed中的该字符连续出现的次数的话，则返回False
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j,count_i,count_j = 0,0,1,0
        while j < len(typed):
            while i < len(name)-1 and name[i] == name[i+1]:
                count_i += 1
                i += 1
            while j < len(typed) and typed[j] == name[i]:
                count_j += 1
                j += 1
            if count_i <= count_j:
                count_i = 1
                count_j = 0
                i += 1
            else:
                return False
        return True if i == len(name) else False
