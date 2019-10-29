# 思路：先将句子按照空格拆分成单词列表，对每一个单词判断首字母是否为元音字母，按照对应规则修改单词，再将单词列表按照空格组合起来
class Solution:
    def toGoatLatin(self, S: str) -> str:
        S_list = S.split(' ')
        vowel = ('a','e','i','o','u','A','E','I','O','U')
        count = 0
        for i in S_list:
            if i[0] in vowel:
                S_list[count] = i + 'ma' + 'a' * (count+1)
            else:
                S_list[count] = i[1:] + i[0] + 'ma' + 'a' * (count+1)
            count += 1
        return ' '.join(S_list)
