# 思路：首先判断首字母是否是大写，如果不是，则判断该单词中最小的字母是否比a小，如果是，则说明有大写字母，不是规范的大写字母
# 如果首字母大写，则判断接下来的字母，如果其余的字母中最大的字母比a还小，说明该单词全部大写，是规范的大写字母
# 如果其余的字母中最小的字母比Z还大，则说明剩余的字母全部都是小写字母，是一个首字母大写的单词，是规范的大写字母
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        if word[0] > 'Z':
            if min(set(word)) < 'a':
                return False
            else:
                return True
        else:
            if max(set(word[1:])) < 'a' or min(set(word[1:])) > 'Z':
                return True
            else:
                return False
