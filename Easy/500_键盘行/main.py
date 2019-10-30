# 思路：首先建立每行键盘的字母集合，判断给定的单词中的所有字母组成的集合是否是其中一个集合的子集，如果是，则存入列表中
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(['Q','q','W','w','E','e','R','r','T','t','Y','y','U','u','I','i','O','o','P','p'])
        row2 = set(['A','a','S','s','D','d','F','f','G','g','H','h','J','j','K','k','L','l'])
        row3 = set(['Z','z','X','x','C','c','V','v','B','b','N','n','M','m'])
        result = []
        for i in words:
            set_i = set(i)
            if set_i.issubset(row1) or set_i.issubset(row2) or set_i.issubset(row3):
                result.append(i)
        return result
