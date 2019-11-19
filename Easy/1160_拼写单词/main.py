# 思路：建立字典保存chars中每个字符出现的频次，遍历words数组中每个单词的每个字符是否都在字典中，并且出现的次数要小于字典中的
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        sum_count = 0
        for i in chars:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for word in words:
            count = 0
            for i in word:
                if i in dic and dic[i] > 0:
                    count += 1
                    dic[i] -= 1
                else:
                    break
            if count == len(word):
                sum_count += count
            for i in range(count):
                dic[word[i]] += 1
        return sum_count
