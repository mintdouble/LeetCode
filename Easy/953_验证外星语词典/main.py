# 思路：将字母和对应顺序映射成字典，比较前一个单词和后一个单词对应位置上字母的顺序
# 如果前一个单词的字母顺序小于后一个单词，则比较下一个单词
# 如果等于后一个单词，则比较下一个字母
# 如果大于后一个单词，则返回False
# 如果后一个单词的所有字母顺序都和前一个单词的前面部分字母顺序相同，则需要比较单词的长度
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True
        dic = {}
        for i in range(26):
            dic[order[i]] = i
        for k in range(len(words)-1):
            i,j = 0,0
            while i < len(words[k]) and j < len(words[k+1]):
                if dic[words[k][i]] < dic[words[k+1][j]]:
                    break
                elif dic[words[k][i]] == dic[words[k+1][j]]:
                    i += 1
                    j += 1
                else:
                    return False
            if i < len(words[k]) and j == len(words[k+1]):
                return False
        return True
