# 思路：按空格分隔字符串后，遍历每个单词，找到匹配第i个单词等于first且第i+1个单词等于second的第i+2个单词，存入third中
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        third = []
        text = text.split(' ')
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                third.append(text[i+2])
        return third
